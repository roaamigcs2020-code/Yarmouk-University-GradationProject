@echo off
setlocal ENABLEDELAYEDEXPANSION

REM Root of the project
set "ROOT=%~dp0"
set "VENV=%ROOT%envSophia312"
set "PY=%VENV%\Scripts\python.exe"

REM Ensure Python 3.12 venv exists
if not exist "%PY%" (
  echo [setup] Creating Python 3.12 virtual environment at "%VENV%"...
  py -3.12 -m venv "%VENV%"
)

REM Upgrade packaging tools
echo [setup] Upgrading pip/setuptools/wheel...
"%PY%" -m pip install --quiet --upgrade pip setuptools wheel

REM Install project dependencies
if exist "%ROOT%requirements.txt" (
  echo [setup] Installing dependencies from requirements.txt...
  "%PY%" -m pip install --quiet -r "%ROOT%requirements.txt"
) else (
  echo [warn] requirements.txt not found; proceeding without dependency installation.
)

REM Launch the app
echo [run] Starting Sophia...
"%PY%" "%ROOT%main.py"

endlocal