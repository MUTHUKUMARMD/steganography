@echo off
REM 🔐 Invisible DRM Platform - Startup Script
REM This script activates the virtual environment and runs the Streamlit app

echo.
echo ======================================================================
echo  🔐 Invisible DRM Platform - Deep Learning Steganography
echo ======================================================================
echo.

REM Check if virtual environment exists
if not exist ".venv" (
    echo ⚠️  Virtual environment not found. Creating one...
    python -m venv .venv
    echo ✅ Virtual environment created.
    echo.
)

REM Activate virtual environment
echo 🚀 Activating virtual environment...
call .venv\Scripts\activate.bat

REM Install dependencies
echo 📦 Installing dependencies from requirements.txt...
pip install -q -r requirements.txt --upgrade

if %ERRORLEVEL% neq 0 (
    echo ❌ Failed to install dependencies.
    echo Please run: pip install -r requirements.txt
    pause
    exit /b 1
)

echo ✅ Dependencies installed successfully.
echo.

REM Run Streamlit app
echo 🌐 Starting Streamlit application...
echo.
echo 📍 App will open at: http://localhost:8501
echo 🛑 Press Ctrl+C to stop the server
echo.

streamlit run streamlit.py

pause
