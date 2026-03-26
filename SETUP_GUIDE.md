# 🔐 Invisible DRM Platform - Complete Setup Guide

## System Requirements

- **OS**: Windows 10/11, macOS, or Linux
- **Python**: 3.8 or higher
- **RAM**: 4 GB minimum (8 GB recommended)
- **Disk Space**: 1 GB for models and dependencies
- **GPU**: Optional (NVIDIA CUDA for faster processing)

## Step-by-Step Installation

### Option 1: Automatic Installation (Windows)

The easiest way to get started:

1. **Navigate to the project folder**
   ```powershell
   cd "c:\Users\dhaks\OneDrive\Desktop\Project - 4\Front-end"
   ```

2. **Double-click `run_app.bat`**
   - The script will automatically:
     - Create a virtual environment (if needed)
     - Install all dependencies
     - Launch the Streamlit application

3. **Wait for the browser to open**
   - Usually opens at `http://localhost:8501`
   - If not, manually navigate to that URL

### Option 2: Manual Installation (All Platforms)

For more control or if automatic setup doesn't work:

1. **Navigate to Front-end directory**
   ```bash
   cd "c:\Users\dhaks\OneDrive\Desktop\Project - 4\Front-end"
   ```

2. **Create a Python virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   
   **Windows (PowerShell):**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   
   **Windows (Command Prompt):**
   ```cmd
   .venv\Scripts\activate.bat
   ```
   
   **Linux/Mac:**
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   streamlit run streamlit.py
   ```

## ✅ Verification Checklist

After installation, verify everything works:

- [ ] Virtual environment activated (you should see `(.venv)` in terminal)
- [ ] All dependencies installed (no errors in pip output)
- [ ] Browser opened to `http://localhost:8501`
- [ ] Streamlit interface loaded successfully
- [ ] Models loaded (check terminal for model loading messages)
- [ ] All menu items visible in sidebar

## 🐛 Troubleshooting

### Issue: "Python is not recognized"
**Solution:** 
- Add Python to PATH during installation
- Or use full path: `C:\Python311\python.exe -m venv .venv`

### Issue: "Permission denied" on activation
**Solution (PowerShell):**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue: Models not loading
**Solution:**
- Verify files exist: `c:\Users\dhaks\OneDrive\Desktop\Project - 4\working\`
  - `encoder_rgb_exact.h5`
  - `decoder_rgb_exact.h5`
- Check file sizes (~590 KB combined)

### Issue: "No module named 'tensorflow'"
**Solution:**
- Reinstall: `pip install --upgrade tensorflow==2.13.0`
- May take 5+ minutes
- Requires ~1.5 GB disk space

### Issue: TensorFlow GPU warnings
**Info:** 
- Normal if no NVIDIA GPU present
- CPU mode will work, just slower
- Safe to ignore

### Issue: "Address already in use"
**Solution:**
- Port 8501 is already in use
- Kill existing Streamlit process
- Or specify different port: `streamlit run streamlit.py --server.port=8502`

## 📂 Checking Model Files

Verify the models are present:

**Windows PowerShell:**
```powershell
Get-ChildItem -Path "..\working" -Filter "*.h5"
```

**Output should show:**
```
encoder_rgb_exact.h5    (260 KB)
decoder_rgb_exact.h5    (333 KB)
```

## 🚀 Quick Start After Installation

### First Time Use

1. **Start the app:** Run `run_app.bat` (or `streamlit run streamlit.py`)
2. **Go to Encode tab**
3. **Upload sample images** (or download from working folder)
4. **Test the workflow:**
   - Encode → Decode → Compare

### Using Example Files

Example images are in `../working/`:
- `cover.jpg` - Sample artwork
- `secret.jpg` - Sample ownership proof
- `stego.png` - Example encoded result
- `recovered.png` - Example extracted proof

## 📦 Dependency Breakdown

What gets installed and why:

| Package | Version | Purpose |
|---------|---------|---------|
| **streamlit** | 1.28.1 | Web UI framework |
| **tensorflow** | 2.13.0 | Deep learning (models) |
| **numpy** | 1.24.3 | Numerical computing |
| **opencv-python** | 4.8.1.78 | Image processing |
| **pillow** | 10.0.1 | Image I/O |
| **matplotlib** | 3.8.0 | Visualization |
| **scikit-image** | 0.21.0 | Advanced image ops |

Total size: ~500 MB (after installation)

## 🔄 Updating Dependencies

To update all packages to latest versions:

```bash
pip install --upgrade -r requirements.txt
```

Or individual package:
```bash
pip install --upgrade tensorflow
```

## 🧹 Cleanup

To uninstall and free up space:

```bash
# Deactivate virtual environment
deactivate

# Delete virtual environment (frees ~500 MB)
rmdir /s .venv          # Windows
rm -rf .venv            # Linux/Mac
```

## 💾 Backup Important Files

Keep backups of:
- Original artwork images
- Secret/proof images used for encoding
- Stego images you want to preserve
- Downloaded metadata JSON files

## 🌐 Accessing the Application

### Local Access (Your Computer)
- **URL**: `http://localhost:8501`
- **Network**: Not accessible from other devices

### To Access from Another Device (Same Network)
1. Find your computer's IP: `ipconfig` (Windows) or `ifconfig` (Linux/Mac)
2. Share URL: `http://<your-ip>:8501`
3. Other device can access over network

### To Deploy Online
Use services like:
- Streamlit Cloud (free)
- Heroku
- AWS, Google Cloud, Azure
- DigitalOcean
- See Streamlit docs for deployment guides

## 🆘 Need More Help?

1. **Check the README.md** in this folder
2. **Review troubleshooting** in README.md
3. **Check model files** exist in `../working/`
4. **Review logs** in terminal where Streamlit runs
5. **Search Streamlit docs**: https://docs.streamlit.io

## ✨ You're Ready!

Once setup is complete:
1. You have a fully functional DRM platform
2. Can encode ownership proofs
3. Can verify ownership on demand
4. Full professional UI with metrics
5. Export capabilities for verification

---

**Last Updated**: March 2026  
**Setup Version**: 1.0  
**Status**: Production Ready ✅
