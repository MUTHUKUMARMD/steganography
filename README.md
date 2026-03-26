# 🔐 Invisible DRM Platform - Front-End

A professional Streamlit web application for embedding and extracting invisible ownership proofs from digital images using deep learning-based steganography.

## 🎯 Features

✅ **Encode** - Hide ownership proof invisibly in artwork  
✅ **Decode** - Extract embedded proof and verify ownership  
✅ **Compare** - Verify ownership by comparing two images  
✅ **Metrics** - View detailed PSNR, SSIM, and hash metrics  
✅ **Download** - Export stego images, proofs, and metadata  
✅ **Professional UI** - Intuitive multi-page interface  

## 📦 Installation

### 1. Navigate to the Front-end directory
```bash
cd "c:\Users\dhaks\OneDrive\Desktop\Project - 4\Front-end"
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
streamlit run streamlit.py
```

The application will open in your default browser at `http://localhost:8501`

## 🚀 Quick Start

### Step 1: Prepare Your Images
- **Artwork**: High-quality image you want to protect (JPG/PNG)
- **Proof**: Your logo or unique ID to hide (JPG/PNG)

### Step 2: Encode (Hide Proof)
1. Click **🔒 Encode** tab
2. Upload artwork image
3. Upload ownership proof
4. Click **🔐 Encode & Hide Proof**
5. Download stego image (looks identical to original!)
6. Share stego image; keep backup of original

### Step 3: Verify Ownership (Later)
1. Click **🔓 Decode** tab
2. Upload the stego image
3. Click **🔓 Extract Hidden Proof**
4. Compare extracted proof with your original
5. Download verification report

### Step 4: Compare Two Images
1. Click **🔍 Compare & Verify** tab
2. Upload leaked and original images
3. Click **🔍 Extract & Compare Ownership Proofs**
4. Get verification verdict

## 📊 Understanding the Metrics

### Stealth Quality
- **Cover-Stego PSNR**: Should be >30 dB (higher = more imperceptible)
- **Cover-Stego SSIM**: Should be >0.99 (1.0 = identical)
- **Max Pixel Diff**: Should be <0.01 (0.005 is imperceptible)
- **Status**: ✅ Imperceptible if Max Diff < 0.01

### Secret Recovery
- **PSNR (dB)**: Should be >20 dB
  - \>30 dB = Excellent quality
  - 20-30 dB = Good quality
  - <20 dB = Degraded

## 🎨 Supported Formats

| Format | Extension | Support |
|--------|-----------|---------|
| JPEG   | .jpg      | ✅ Recommended |
| JPEG   | .jpeg     | ✅ Recommended |
| PNG    | .png      | ✅ Full support |

## 🔧 Requirements

- Python 3.8+
- TensorFlow 2.13+
- Streamlit 1.28+
- All listed in `requirements.txt`

## 📁 File Structure

```
Front-end/
├── streamlit.py              # Main application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── .streamlit/
    └── config.toml          # (auto-generated)
```

## 🎯 How It Works

### Encoding Process
```
Artwork + Proof → Encoder Network → Stego Image (imperceptible changes)
```

### Decoding Process
```
Stego Image → Decoder Network → Recovered Proof (extracted)
```

### Comparison Process
```
Leaked Image → Extract Proof A → Compare → PSNR/SSIM → Verdict
Original Image → Extract Proof B → Calculate → Same Owner?
```

## 📈 Technical Details

### Image Processing
- Input size: Arbitrary (auto-resized to 128×128)
- Output size: 128×128 (matched network architecture)
- Color space: RGB only
- Value range: [0, 1] (normalized)

### Models
- **Encoder**: `encoder_rgb_exact.h5` (~333 KB)
- **Decoder**: `decoder_rgb_exact.h5` (~260 KB)
- Both loaded from: `../working/`

### Metrics Computed
- **PSNR** (Peak Signal-to-Noise Ratio): Image quality measure
- **SSIM** (Structural Similarity Index): Perceptual similarity
- **SHA256 Hashes**: Unique image fingerprints
- **Statistics**: Mean, std, min, max pixel values

## ⚙️ Configuration

The app uses sensible defaults:
- IMG_SIZE = 128×128 pixels
- Batch processing via Keras predict()
- Automatic GPU detection (if available)

No configuration file needed for basic usage.

## 🐛 Troubleshooting

### Models not found
**Error**: `Failed to load models`  
**Solution**: Ensure `encoder_rgb_exact.h5` and `decoder_rgb_exact.h5` exist in `../working/`

### Image too small
**Error**: `OpenCV Error`  
**Solution**: Use images at least 64×64 pixels

### Memory error
**Error**: `ResourceExhaustedError`  
**Solution**: Close other applications or use smaller images

### TensorFlow warnings
**Info**: Normal TensorFlow startup messages  
**Action**: Safe to ignore

## 📜 Usage Rights & Legal

- For personal use and legal verification of ownership
- Not for malicious purposes
- Always verify through legal channels for intellectual property disputes
- Keep backups of your original secret images

## 📚 Learn More

See `../working/README.md` and `../working/SOLUTION_SUMMARY.md` for technical details on the steganography implementation.

## 🎓 Educational Resources

This project demonstrates:
- ✅ Deep Learning (CNN architecture)
- ✅ Image Processing (OpenCV)
- ✅ Steganography (information hiding)
- ✅ Loss function design (multi-term optimization)
- ✅ Data augmentation
- ✅ Model evaluation metrics
- ✅ Web UI with Streamlit

## 📞 Support

For issues or improvements:
1. Check the troubleshooting section
2. Review model files exist
3. Ensure all dependencies installed
4. Check system has sufficient RAM

## 📝 License

This project is part of the "Invisible DRM Platform" series.
All rights reserved © 2026.

---

**Last Updated**: March 2026  
**Version**: 1.0  
**Status**: Production Ready ✅
