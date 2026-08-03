@echo off
setlocal
cd /d "%~dp0"

set "PYTHON_CMD="

where py >nul 2>nul
if not errorlevel 1 (
    py -3.11 --version >nul 2>nul
    if not errorlevel 1 set "PYTHON_CMD=py -3.11"
)

if not defined PYTHON_CMD (
    where python >nul 2>nul
    if not errorlevel 1 set "PYTHON_CMD=python"
)

if not defined PYTHON_CMD (
    where python3 >nul 2>nul
    if not errorlevel 1 set "PYTHON_CMD=python3"
)

if not defined PYTHON_CMD goto :python_missing

echo Python gevonden via: %PYTHON_CMD%
%PYTHON_CMD% --version

if not exist ".venv\Scripts\python.exe" (
    echo Virtuele omgeving wordt aangemaakt...
    %PYTHON_CMD% -m venv .venv
    if errorlevel 1 goto :error
)

call .venv\Scripts\activate.bat
if errorlevel 1 goto :error

python -m pip install --upgrade pip
if errorlevel 1 goto :error

python -m pip install -r requirements.txt
if errorlevel 1 goto :error

python -m streamlit run app.py
exit /b 0

:python_missing
echo.
echo Python is niet gevonden op deze computer.
echo Installeer bij voorkeur Python 3.11 en vink "Add Python to PATH" aan.
echo Daarna dit startbestand opnieuw uitvoeren.
echo.
echo Snelle installatie via PowerShell:
echo winget install Python.Python.3.11
pausE
exit /b 1

:error
echo.
echo Installatie of starten is mislukt.
echo Controleer de foutmelding hierboven.
pause
exit /b 1
