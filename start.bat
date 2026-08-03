@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo Virtuele omgeving wordt aangemaakt...
    py -3.11 -m venv .venv
    if errorlevel 1 goto :error
)

call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 goto :error

streamlit run app.py
exit /b 0

:error
echo.
echo Installatie of starten is mislukt.
pause
exit /b 1
