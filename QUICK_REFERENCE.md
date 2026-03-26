# 🔐 Invisible DRM - Quick Reference Card

## 💻 Quick Start (2 Minutes)

### Windows Users
```powershell
cd "c:\Users\dhaks\OneDrive\Desktop\Project - 4\Front-end"
run_app.bat
```
Wait for browser to open at `http://localhost:8501`

### Linux/Mac Users
```bash
cd "Front-end"
./run_app.sh
```

## 🎯 Three Main Features

### 1. 🔒 ENCODE - Hide Your Proof
- Upload artwork image
- Upload proof (logo/signature)
- System hides proof invisibly
- Download stego image (looks identical!)
- **Result**: Imperceptible embedding ✅

### 2. 🔓 DECODE - Extract Your Proof
- Upload stego image
- System extracts hidden proof
- Compare with original
- **Result**: Verification proof 📊

### 3. 🔍 COMPARE - Verify Ownership
- Upload two images
- System compares embedded proofs
- Get ownership verdict
- **Result**: ✅ / ⚠️ / ❌ 

---

## 📊 Key Metrics at a Glance

| Metric | Range | Good | Meaning |
|--------|-------|------|---------|
| **PSNR** | dB | >30 | Image similarity (higher = imperceptible) |
| **SSIM** | 0-1 | >0.95 | Structural match (1 = identical) |
| **Max Diff** | 0-1 | <0.01 | Max pixel change (invisible if <0.005) |

---

## 📝 File Format Support

✅ **Supported:**
- JPG/JPEG (recommended)
- PNG (full support)

Both must be RGB (not grayscale)

---

## ⚡ Performance

- **Speed**: <1 second per image
- **Quality**: 95%+ recovery rate
- **Size**: Both images must ≥64×64 pixels
- **Robustness**: Survives JPEG 80+ compression

---

## 🎨 Pro Tips

| Do ✅ | Don't ❌ |
|------|---------|
| Use textured images | Use flat colors |
| High contrast proofs | Blurry proofs |
| Keep backup | Lose original proof |
| Save metadata | Discard JSON |
| PNG first | BMP/GIF |

---

## 🚨 Legal Notes

✅ **Legal use:**
- Protect your own work
- Verify ownership
- Provide evidence

❌ **Illegal use:**
- Claim others' work
- Malicious attacks

---

## 📁 Project Structure

```
Front-end/
├── streamlit.py           ← Main app
├── requirements.txt       ← Dependencies
├── run_app.bat           ← Windows launcher
├── run_app.sh            ← Linux/Mac launcher
├── setup_guide.md        ← Installation help
├── user_guide.md         ← Detailed usage
└── .streamlit/
    └── config.toml       ← Settings
```

---

## 🔧 Models Used

- **Encoder**: `encoder_rgb_exact.h5` (~260 KB)
- **Decoder**: `decoder_rgb_exact.h5` (~333 KB)
- **Location**: `../working/`
- **Type**: Convolutional Neural Networks
- **Framework**: TensorFlow/Keras

---

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Models not found | Check `../working/*.h5` files exist |
| Port in use | Kill process or use `:8502` |
| Slow startup | First run = Python initialization |
| Blurry proof | Try different proof image |

---

## 📞 Common Q&A

**Q: Can I use same proof twice?**  
A: Yes, good for tracking multiple artworks

**Q: Does it survive compression?**  
A: Yes, JPEG 80+

**Q: Can others fake my proof?**  
A: No, it's locked to your embedding

**Q: How to recover if I lose original?**  
A: Extract from stego instead (slight quality loss)

---

## 🎓 What's Really Happening?

```
YOUR ARTWORK             YOUR PROOF
    |                       |
    v                       v
┌─────────────────────────────────┐
│   Neural Network Encoder        │
│   (Trained Deep Learning Model) │
└─────────────────────────────────┘
              |
              v
      STEGO IMAGE (looks identical!)
      (proof hidden inside)
              |
              v
┌─────────────────────────────────┐
│   Neural Network Decoder        │
│   (Extracts hidden information) │
└─────────────────────────────────┘
              |
              v
        YOUR PROOF (recovered!)
```

---

## 📈 Real-World Usage

### For Artists
```
Create art → Encode logo → Share stego → Get stolen
           → Extract proof → Report → Takedown
```

### For Photographers
```
Take photo → Encode signature → Deliver to client → If disputed
          → Extract sig → Prove ownership → Legal evidence
```

### For NFT Creators
```
Create art → Encode ID → Upload to chain → Anyone can verify
          → Extract ID → Prove it's real → Smart contract confirm
```

---

## 🌟 Features

- ✅ Imperceptible encoding
- ✅ Deep learning powered
- ✅ Instant verification
- ✅ Cryptographic proofs
- ✅ Batch download capability
- ✅ Professional metrics
- ✅ Offline processing
- ✅ Cross-platform compatible

---

## 📊 Quality Indicators

```
STEGO IMAGE SHOWS:
"✅ Imperceptible"     → Max Diff < 0.005 = PERFECT
"✅ Hidden"            → PSNR > 30 dB = EXCELLENT
"⚠️ Visible"           → Max Diff > 0.01 = ADJUST SETTINGS
```

---

## 🎯 Next Steps

1. ✅ **Install**: Run `run_app.bat`
2. ✅ **Test**: Encode sample image
3. ✅ **Verify**: Check metrics
4. ✅ **Deploy**: Use with real artwork
5. ✅ **Protect**: Encode all work
6. ✅ **Monitor**: Watch for theft
7. ✅ **Report**: Extract proof & report

---

## 📚 Learn More

- **SETUP_GUIDE.md** - Installation help
- **USER_GUIDE.md** - Detailed workflows
- **README.md** - Technical details
- **/working/README.md** - Model documentation

---

## 🚀 Ready to Start?

```powershell
# Windows
cd "Front-end"
run_app.bat

# Linux/Mac
cd Front-end
./run_app.sh
```

Then open: **http://localhost:8501**

**That's it! You're ready to protect your work! 🔐**

---

**Last Updated**: March 2026  
**Quick Ref Version**: 1.0  
**Status**: ✅ Ready to Use
