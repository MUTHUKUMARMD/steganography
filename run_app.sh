#!/bin/bash
# 🔐 Invisible DRM Platform - Startup Script (Linux/Mac)
# This script activates the virtual environment and runs the Streamlit app

echo ""
echo "========================================================================"
echo "  🔐 Invisible DRM Platform - Deep Learning Steganography"
echo "========================================================================"
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "⚠️  Virtual environment not found. Creating one..."
    python3 -m venv .venv
    echo "✅ Virtual environment created."
    echo ""
fi

# Activate virtual environment
echo "🚀 Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies from requirements.txt..."
pip install -q -r requirements.txt --upgrade

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies."
    echo "Please run: pip install -r requirements.txt"
    exit 1
fi

echo "✅ Dependencies installed successfully."
echo ""

# Run Streamlit app
echo "🌐 Starting Streamlit application..."
echo ""
echo "📍 App will open at: http://localhost:8501"
echo "🛑 Press Ctrl+C to stop the server"
echo ""

streamlit run streamlit.py
