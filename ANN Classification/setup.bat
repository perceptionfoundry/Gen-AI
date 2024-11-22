@echo off

REM Check if Conda is installed
where conda >nul 2>nul
if %errorlevel% neq 0 (
    echo Conda is not installed. Please install Conda before proceeding.
    exit /b 1
)

REM Environment name (change this if needed)
set ENV_NAME=venv

REM Create the Conda environment
echo Creating Conda environment: %ENV_NAME%...
conda create -y -n %ENV_NAME% python=3.12  

REM Activate the environment
echo Activating Conda environment...
call conda activate %ENV_NAME%

REM Install dependencies

if exist requirements.txt (
    echo Installing dependencies from requirements.txt...
    pip install -r requirements.txt
) else (
    echo  requirements.txt found. Skipping dependency installation.
)

echo Setup complete! Activate the environment with: conda activate %ENV_NAME%
