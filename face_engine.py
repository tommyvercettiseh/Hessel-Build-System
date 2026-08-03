from __future__ import annotations

import hashlib
import pickle
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import cv2
import numpy as np
from insightface.app import FaceAnalysis
from sklearn.cluster import DBSCAN

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
CACHE_DIRNAME = ".facedetect"
CACHE_FILENAME = "cache.pkl"


@dataclass
class FaceRecord:
    image_path: str
    face_index: int
    bbox: tuple[int, int, int, int]
    embedding: np.ndarray
    detection_score: float
    cluster_id: int = -1


@dataclass
class ScanResult:
    source_dir: str
    image_paths: list[str]
    faces: list[FaceRecord]
    no_face_images: list[str]


def discover_images(source_dir: str | Path) -> list[Path]:
    root = Path(source_dir).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise ValueError(f"Ongeldige fotomap: {root}")

    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file()
        and path.suffix.lower() in SUPPORTED_EXTENSIONS
        and CACHE_DIRNAME not in path.parts
    )


def get_face_model() -> FaceAnalysis:
    model = FaceAnalysis(
        name="buffalo_l",
        providers=["CPUExecutionProvider"],
    )
    model.prepare(ctx_id=-1, det_size=(640, 640))
    return model


def scan_folder(
    source_dir: str | Path,
    min_detection_score: float = 0.55,
    progress_callback=None,
) -> ScanResult:
    image_paths = discover_images(source_dir)
    if not image_paths:
        raise ValueError("Geen ondersteunde afbeeldingen gevonden.")

    model = get_face_model()
    face_records: list[FaceRecord] = []
    no_face_images: list[str] = []

    for index, image_path in enumerate(image_paths, start=1):
        image = cv2.imread(str(image_path))
        if image is None:
            no_face_images.append(str(image_path))
            continue

        detected = model.get(image)
        accepted = []
        for face_index, face in enumerate(detected):
            score = float(face.det_score)
            if score < min_detection_score:
                continue

            x1, y1, x2, y2 = [int(value) for value in face.bbox]
            embedding = np.asarray(face.normed_embedding, dtype=np.float32)
            accepted.append(
                FaceRecord(
                    image_path=str(image_path),
                    face_index=face_index,
                    bbox=(x1, y1, x2, y2),
                    embedding=embedding,
                    detection_score=score,
                )
            )

        if accepted:
            face_records.extend(accepted)
        else:
            no_face_images.append(str(image_path))

        if progress_callback:
            progress_callback(index, len(image_paths), image_path.name)

    return ScanResult(
        source_dir=str(Path(source_dir).resolve()),
        image_paths=[str(path) for path in image_paths],
        faces=face_records,
        no_face_images=no_face_images,
    )


def cluster_faces(
    result: ScanResult,
    similarity_threshold: float = 0.48,
    min_samples: int = 2,
) -> ScanResult:
    if not result.faces:
        return result

    embeddings = np.stack([face.embedding for face in result.faces])
    distance_threshold = max(0.05, min(0.95, 1.0 - similarity_threshold))
    labels = DBSCAN(
        eps=distance_threshold,
        min_samples=min_samples,
        metric="cosine",
        n_jobs=-1,
    ).fit_predict(embeddings)

    next_singleton = int(labels.max()) + 1 if labels.size else 0
    for face, label in zip(result.faces, labels, strict=True):
        if int(label) == -1:
            face.cluster_id = next_singleton
            next_singleton += 1
        else:
            face.cluster_id = int(label)

    return result


def cache_path(source_dir: str | Path) -> Path:
    return Path(source_dir) / CACHE_DIRNAME / CACHE_FILENAME


def save_cache(result: ScanResult) -> Path:
    path = cache_path(result.source_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as handle:
        pickle.dump(result, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return path


def load_cache(source_dir: str | Path) -> ScanResult | None:
    path = cache_path(source_dir)
    if not path.exists():
        return None
    with path.open("rb") as handle:
        loaded = pickle.load(handle)
    if not isinstance(loaded, ScanResult):
        return None
    return loaded


def faces_by_cluster(result: ScanResult) -> dict[int, list[FaceRecord]]:
    grouped: dict[int, list[FaceRecord]] = {}
    for face in result.faces:
        grouped.setdefault(face.cluster_id, []).append(face)
    return dict(sorted(grouped.items(), key=lambda item: len(item[1]), reverse=True))


def image_face_counts(result: ScanResult) -> dict[str, int]:
    counts: dict[str, int] = {path: 0 for path in result.image_paths}
    for face in result.faces:
        counts[face.image_path] = counts.get(face.image_path, 0) + 1
    return counts


def images_for_cluster(
    result: ScanResult,
    cluster_id: int,
    include_group_photos: bool,
) -> list[str]:
    counts = image_face_counts(result)
    paths = {face.image_path for face in result.faces if face.cluster_id == cluster_id}
    if not include_group_photos:
        paths = {path for path in paths if counts.get(path, 0) == 1}
    return sorted(paths)


def multi_person_images(result: ScanResult) -> list[str]:
    counts = image_face_counts(result)
    return sorted(path for path, count in counts.items() if count >= 2)


def crop_face(face: FaceRecord, padding: float = 0.25) -> np.ndarray | None:
    image = cv2.imread(face.image_path)
    if image is None:
        return None

    height, width = image.shape[:2]
    x1, y1, x2, y2 = face.bbox
    box_width = x2 - x1
    box_height = y2 - y1
    x1 = max(0, int(x1 - box_width * padding))
    y1 = max(0, int(y1 - box_height * padding))
    x2 = min(width, int(x2 + box_width * padding))
    y2 = min(height, int(y2 + box_height * padding))
    crop = image[y1:y2, x1:x2]
    if crop.size == 0:
        return None
    return cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)


def safe_folder_name(name: str) -> str:
    invalid = '<>:"/\\|?*'
    cleaned = "".join("_" if char in invalid else char for char in name).strip()
    return cleaned or "Onbekend"


def copy_images(paths: Iterable[str], destination: str | Path) -> tuple[int, list[str]]:
    destination_path = Path(destination).expanduser().resolve()
    destination_path.mkdir(parents=True, exist_ok=True)

    copied = 0
    errors: list[str] = []
    for source in paths:
        source_path = Path(source)
        try:
            target = destination_path / source_path.name
            if target.exists():
                digest = hashlib.sha1(str(source_path).encode("utf-8")).hexdigest()[:8]
                target = destination_path / f"{source_path.stem}_{digest}{source_path.suffix}"
            shutil.copy2(source_path, target)
            copied += 1
        except OSError as exc:
            errors.append(f"{source_path}: {exc}")
    return copied, errors
