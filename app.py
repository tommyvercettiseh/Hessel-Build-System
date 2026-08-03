from __future__ import annotations

from pathlib import Path
import tkinter as tk
from tkinter import filedialog

import streamlit as st

from face_engine import (
    cluster_faces,
    copy_images,
    crop_face,
    faces_by_cluster,
    images_for_cluster,
    load_cache,
    multi_person_images,
    safe_folder_name,
    save_cache,
    scan_folder,
)

st.set_page_config(page_title="FaceDetect", page_icon="🧠", layout="wide")


def choose_directory(title: str) -> str:
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    selected = filedialog.askdirectory(title=title)
    root.destroy()
    return selected


def cluster_name(cluster_id: int) -> str:
    return st.session_state.names.get(cluster_id, f"Persoon {cluster_id + 1}")


def render_gallery(paths: list[str], limit: int = 60) -> None:
    if not paths:
        st.info("Geen foto's voor deze selectie.")
        return

    columns = st.columns(4)
    for index, image_path in enumerate(paths[:limit]):
        with columns[index % 4]:
            st.image(image_path, use_container_width=True)
            st.caption(Path(image_path).name)
    if len(paths) > limit:
        st.caption(f"Preview toont {limit} van {len(paths)} foto's.")


if "source_dir" not in st.session_state:
    st.session_state.source_dir = ""
if "result" not in st.session_state:
    st.session_state.result = None
if "names" not in st.session_state:
    st.session_state.names = {}
if "destination_dir" not in st.session_state:
    st.session_state.destination_dir = ""

st.title("🧠 FaceDetect")
st.write("Selecteer een fotomap, bekijk de unieke gezichten en sorteer daarna pas de foto's.")

with st.sidebar:
    st.header("Instellingen")
    similarity = st.slider(
        "Overeenkomst voor dezelfde persoon",
        min_value=0.30,
        max_value=0.75,
        value=0.48,
        step=0.01,
        help="Hoger is strenger en maakt sneller meerdere losse groepen van dezelfde persoon.",
    )
    detection_score = st.slider(
        "Minimale gezichtsscore",
        min_value=0.30,
        max_value=0.95,
        value=0.55,
        step=0.05,
    )
    min_samples = st.selectbox(
        "Minimaal gezichten per automatische groep",
        options=[1, 2, 3, 4],
        index=1,
    )

st.subheader("1. Fotomap kiezen")
left, right = st.columns([1, 3])
with left:
    if st.button("📁 Kies fotomap", use_container_width=True):
        selected = choose_directory("Kies de map met foto's")
        if selected:
            st.session_state.source_dir = selected
            cached = load_cache(selected)
            if cached:
                st.session_state.result = cached
                st.success("Bestaande scan geladen.")
with right:
    st.text_input("Bronmap", key="source_dir", placeholder=r"C:\Foto's\Vakantie")

source_dir = st.session_state.source_dir.strip()
if source_dir and not Path(source_dir).is_dir():
    st.warning("Deze bronmap bestaat niet.")

scan_col, cache_col = st.columns([1, 2])
with scan_col:
    start_scan = st.button(
        "🔍 Scan gezichten",
        type="primary",
        disabled=not source_dir or not Path(source_dir).is_dir(),
        use_container_width=True,
    )
with cache_col:
    st.caption("De eerste scan downloadt een lokaal AI-model en kan daardoor langer duren.")

if start_scan:
    progress = st.progress(0.0, text="Scan wordt gestart…")

    def update_progress(current: int, total: int, filename: str) -> None:
        progress.progress(current / total, text=f"{current}/{total}: {filename}")

    try:
        with st.spinner("Gezichten detecteren en kenmerken berekenen…"):
            result = scan_folder(
                source_dir,
                min_detection_score=detection_score,
                progress_callback=update_progress,
            )
            result = cluster_faces(
                result,
                similarity_threshold=similarity,
                min_samples=min_samples,
            )
            save_cache(result)
            st.session_state.result = result
            st.session_state.names = {}
        progress.empty()
        st.success("Scan voltooid. Controleer nu de persoonsgroepen.")
    except Exception as exc:
        progress.empty()
        st.exception(exc)

result = st.session_state.result
if result is None:
    st.stop()

groups = faces_by_cluster(result)
st.divider()
st.subheader("2. Preview van unieke gezichten")
metric_cols = st.columns(4)
metric_cols[0].metric("Foto's", len(result.image_paths))
metric_cols[1].metric("Gezichten", len(result.faces))
metric_cols[2].metric("Persoonsgroepen", len(groups))
metric_cols[3].metric("Zonder gezicht", len(result.no_face_images))

if not groups:
    st.warning("Er zijn geen gezichten gevonden met de huidige instellingen.")
else:
    st.caption("Geef groepen een naam. Losse groepen kunnen dezelfde persoon zijn wanneer foto's sterk verschillen.")
    cards = st.columns(5)
    for index, (cluster_id, faces) in enumerate(groups.items()):
        with cards[index % 5]:
            preview = crop_face(faces[0])
            if preview is not None:
                st.image(preview, use_container_width=True)
            new_name = st.text_input(
                "Naam",
                value=st.session_state.names.get(cluster_id, f"Persoon {cluster_id + 1}"),
                key=f"name_{cluster_id}",
                label_visibility="collapsed",
            )
            st.session_state.names[cluster_id] = new_name.strip() or f"Persoon {cluster_id + 1}"
            unique_photos = len({face.image_path for face in faces})
            st.caption(f"{unique_photos} foto's · {len(faces)} gezichten")

st.divider()
st.subheader("3. Foto's filteren en previewen")

mode = st.radio(
    "Welke foto's wil je selecteren?",
    options=[
        "Gekozen persoon",
        "Alle foto's met meerdere personen",
        "Foto's zonder herkend gezicht",
    ],
    horizontal=True,
)

selected_paths: list[str] = []
destination_name = "Selectie"

if mode == "Gekozen persoon" and groups:
    label_to_id = {
        f"{cluster_name(cluster_id)} ({len({face.image_path for face in faces})} foto's)": cluster_id
        for cluster_id, faces in groups.items()
    }
    selected_label = st.selectbox("Kies persoon", options=list(label_to_id))
    chosen_cluster = label_to_id[selected_label]
    include_group_photos = st.radio(
        "Welke regel moet gelden?",
        options=[
            "Alleen foto's waarop deze persoon alleen staat",
            "Ook foto's waarop andere personen staan",
        ],
        horizontal=True,
    ) == "Ook foto's waarop andere personen staan"
    selected_paths = images_for_cluster(result, chosen_cluster, include_group_photos)
    destination_name = safe_folder_name(cluster_name(chosen_cluster))

elif mode == "Alle foto's met meerdere personen":
    selected_paths = multi_person_images(result)
    destination_name = "Meerdere_personen"

elif mode == "Foto's zonder herkend gezicht":
    selected_paths = result.no_face_images
    destination_name = "Geen_gezicht"

st.info(f"Deze selectie bevat **{len(selected_paths)} foto's**.")
render_gallery(selected_paths)

st.divider()
st.subheader("4. Kopiëren naar uitvoermap")
output_left, output_right = st.columns([1, 3])
with output_left:
    if st.button("📂 Kies uitvoermap", use_container_width=True):
        selected = choose_directory("Kies de uitvoermap")
        if selected:
            st.session_state.destination_dir = selected
with output_right:
    st.text_input("Uitvoermap", key="destination_dir", placeholder=r"C:\Foto's\Gesorteerd")

base_destination = st.session_state.destination_dir.strip()
final_destination = str(Path(base_destination) / destination_name) if base_destination else ""
if final_destination:
    st.caption(f"Bestemming: `{final_destination}`")

if st.button(
    "✅ Kopieer selectie",
    type="primary",
    disabled=not selected_paths or not base_destination,
):
    copied, errors = copy_images(selected_paths, final_destination)
    st.success(f"{copied} foto's gekopieerd naar {final_destination}")
    if errors:
        with st.expander(f"{len(errors)} fouten"):
            st.code("\n".join(errors))
