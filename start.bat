@echo off
setlocal EnableExtensions
cd /d "%~dp0"

set "PYTHON_CMD="

rem Prefer the Windows Python launcher when Python 3.11 is installed.
where py >nul 2>nul
if not errorlevel 1 (
    py -3.11 --version >nul 2>nul
    if not errorlevel 1 set "PYTHON_CMD=py -3.11"
)

rem Common per-user Python 3.11 installation path.
if not defined PYTHON_CMD (
    if exist "%LocalAppData%\Programs\Python\Python311\python.exe" (
        set "PYTHON_CMD=%LocalAppData%\Programs\Python\Python311\python.exe"
    )
)

rem Common all-users Python 3.11 installation path.
if not defined PYTHON_CMD (
    if exist "%ProgramFiles%\Python311\python.exe" (
        set "PYTHON_CMD=%ProgramFiles%\Python311\python.exe"
    )
)

if not defined PYTHON_CMD goto :python_missing

echo Python 3.11 gevonden via: %PYTHON_CMD%
%PYTHON_CMD% --version

rem Remove an environment created with the wrong Python version.
if exist ".venv\Scripts\python.exe" (
    for /f "tokens=2" %%V in ('".venv\Scripts\python.exe" -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"') do set "VENV_VERSION=%%V"
    if not "%VENV_VERSION%"=="3.11" (
        echo Bestaande virtuele omgeving gebruikt Python %VENV_VERSION% en wordt opnieuw aangemaakt...
        rmdir /s /q .venv
    )
)

if not exist ".venv\Scripts\python.exe" (
    echo Virtuele omgeving wordt aangemaakt met Python 3.11...
    "%PYTHON_CMD%" -m venv .venv
    if errorlevel 1 goto :error
)

call .venv\Scripts\activate.bat
if errorlevel 1 goto :error

python -m pip install --upgrade pip
if errorlevel 1 goto :error

python -m pip install --only-binary=:all: numpy==1.26.4
if errorlevel 1 goto :error

python -m pip install -r requirements.txt
if errorlevel 1 goto :error

python -m streamlit run app.py
exit /b 0

:python_missing
echo.
echo Python 3.11 is niet gevonden.
echo Deze app werkt momenteel niet met jouw Python 3.13-installatie.
echo.
echo Voer in PowerShell uit:
echo winget install --id Python.Python.3.11 -e
 echo.
echo Sluit PowerShell daarna volledig af, open opnieuw en start start.bat.
pause
exit /b 1

:error
echo.
echo Installatie of starten is mislukt.
echo Controleer de foutmelding hierboven.
pause
exit /b 1
