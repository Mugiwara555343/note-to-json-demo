@echo off
echo ========================================
echo    Memory Watcher - Starting Up
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Check if requirements are installed
echo Checking dependencies...
pip show watchdog >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
)

echo.
echo ========================================
echo    Starting Memory Watcher...
echo ========================================
echo.
echo Watching for .md file changes in:
echo   - demo_entries/ folder
echo.
echo Press Ctrl+C to stop the watcher
echo.

REM Start the memory watcher
python memory_watcher.py

echo.
echo Memory Watcher stopped.
pause 