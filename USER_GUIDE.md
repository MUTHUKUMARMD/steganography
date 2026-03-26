# 🔐 Invisible DRM Platform - User Guide

Welcome to the Invisible DRM Platform! This guide walks you through real-world usage scenarios.

## 🎯 Common Workflows

### Scenario 1: Digital Artist Protecting Their Artwork

**Goal:** Hide your studio logo invisibly in your artwork before sharing online

**Steps:**

1. **Prepare Your Images**
   - Artwork: Your final digital painting (PNG/JPG)
   - Logo: Your studio's colored logo (PNG with white background recommended)

2. **Launch the App**
   - Click `run_app.bat` or run `streamlit run streamlit.py`

3. **Encode the Proof**
   - Click **🔒 Encode** tab
   - Upload your artwork
   - Upload your studio logo
   - Click **🔐 Encode & Hide Proof**
   - Wait 2-10 seconds for processing

4. **Verify It Worked**
   - View the side-by-side comparison
   - Check metrics:
     - Max Diff should be < 0.01
     - PSNR should be > 30 dB
     - Status should say "Imperceptible" ✅

5. **Download & Share**
   - Download "Stego Image" (this is what you share)
   - Back up "Recovered Proof Verification" (for proof)
   - Back up "Metadata" JSON (for records)
   - Post stego image on social media, portfolio, NFT platform

6. **If Your Work Gets Stolen**
   - Locate leaked image
   - See Scenario 3 below

---

### Scenario 2: Photographer Verifying Image Authenticity

**Goal:** Prove that a photo in your portfolio is authentic (not AI-generated or fake)

**Setup:**
- Before sharing: Hide your signature/timestamp invisibly
- Later: Extract and prove it's your original

**Steps:**

1. **Initial Encoding (When Creating Portfolio)**
   - Artwork: Your raw photograph
   - Proof: Your photographer's signature or timestamp with date
   - Follow steps 1-5 from Scenario 1
   - Keep backup of original signature image

2. **Later Verification (When Authenticity Questioned)**
   - Go to **🔓 Decode** tab
   - Upload the photograph in question
   - Click **🔓 Extract Hidden Proof**
   - Compare extracted signature with your original
   - You now have cryptographic proof it's your original!

---

### Scenario 3: Catching Unauthorized Image Use

**Goal:** Detect if someone used your artwork without permission

**Steps:**

1. **You Spot a Suspicious Image**
   - Found on another website, social media, or NFT platform
   - Looks similar to your work

2. **Extract Hidden Proof**
   - Go to **🔓 Decode** tab
   - Upload the suspicious image
   - Click **🔓 Extract Hidden Proof**
   - A clear proof image appears!
   - Compare with your original proof

3. **If It Matches:**
   - ✅ This proves your ownership
   - Download the extracted proof + metadata
   - Use as evidence for DMCA takedown
   - Report to platform (YouTube, Instagram, OpenSea, etc.)

4. **If It Doesn't Match:**
   - The image is probably not yours
   - Or it's a heavily modified version

---

### Scenario 4: Comparing Two Versions of Your Work

**Goal:** Verify if leaked image is actually your artwork or something else

**Setup:**
- You have: Backup stego image + leaked/disputed image

**Steps:**

1. **Go to Compare Tab**
   - Click **🔍 Compare & Verify**

2. **Upload Both Images**
   - Image A: Leaked/disputed image
   - Image B: Your backup stego image

3. **Extract & Compare**
   - Click **🔍 Extract & Compare Ownership Proofs**
   - System extracts proof from both images
   - Shows PSNR and SSIM metrics
   - Gives ownership verdict:
     - ✅ OWNERSHIP VERIFIED
     - ⚠️ PARTIAL MATCH
     - ❌ NO MATCH

4. **Use the Verdict**
   - If ✅ Verified: Legal evidence of ownership
   - If ⚠️ Partial: Image was modified
   - If ❌ No Match: Different artwork

---

## 📊 Understanding the Metrics

### What Do These Numbers Mean?

**PSNR (Peak Signal-to-Noise Ratio) - in dB**
- Measures image quality
- Higher = better quality
- >30 dB: Excellent (imperceptible changes)
- 20-30 dB: Good
- <20 dB: Noticeable degradation

**SSIM (Structural Similarity Index)**
- Ranges from 0 to 1 (1 = identical)
- >0.95: Very similar (human eye can't tell difference)
- 0.85-0.95: Similar with minor differences
- <0.85: Noticeably different

**Max Difference**
- Maximum pixel value change (0-1 scale)
- <0.005: Imperceptible (1 pixel difference)
- 0.005-0.01: Very subtle
- >0.01: Noticeable

**Hash**
- SHA256 fingerprint of image
- Unique identifier
- Useful for tracking versions

### Good vs Bad Results

**✅ GOOD ENCODING:**
```
Cover-Stego PSNR:  32.5 dB (>30 = excellent)
Cover-Stego SSIM:  0.998   (>0.95 = excellent)
Max Diff:          0.004   (<0.005 = imperceptible)
Secret PSNR:       28.3 dB (>20 = good)
Status:            ✅ Imperceptible
```

**⚠️ ACCEPTABLE:**
```
Cover-Stego PSNR:  24.2 dB (>20 = okay)
Cover-Stego SSIM:  0.92    (>0.85 = acceptable)
Max Diff:          0.008   (<0.01 = subtle)
Secret PSNR:       22.5 dB (>20 = good)
Status:            ⚠️ Visible on close inspection
```

**❌ POOR ENCODING:**
```
Cover-Stego PSNR:  18.1 dB (<20 = bad)
Cover-Stego SSIM:  0.78    (<0.85 = noticeable)
Max Diff:          0.02    (>0.01 = very visible)
Secret PSNR:       15.2 dB (<20 = blurry)
Status:            ❌ Visible changes
```

---

## 🎨 Tips for Best Results

### Choosing Artwork
✅ **Good artwork for encoding:**
- Complex textures (photos, paintings)
- Natural patterns (don't reveal changes easily)
- 256×256 pixels or larger
- High-resolution images

❌ **Avoid:**
- Simple solid colors
- Geometric patterns
- Gradients (changes will show)
- Small images (<64×64)

### Choosing Proof Images
✅ **Good proof images:**
- High contrast (white on black, colored on white)
- Recognizable patterns (logos, signatures)
- 100×100 pixels or larger
- Simple and bold designs

❌ **Avoid:**
- Photography (blurs too much)
- Fine details
- Thin lines (may disappear)
- Very small text

### File Formats
✅ **Use:**
- PNG (recommended, lossless)
- JPG quality 85+ (acceptable)

❌ **Avoid:**
- BMP (not optimized)
- GIF (limited colors)
- WEBP (may have compatibility issues)

---

## ⚠️ Important Considerations

### What the System Can & Cannot Do

✅ **CAN:**
- Hide information imperceptibly
- Survive compression (JPEG 80+)
- Survive basic cropping (partial images still have proof)
- Provide cryptographic evidence
- Work offline
- Process instantly

❌ **CANNOT:**
- Survive extreme modifications (resizing <50%, heavy filters)
- Work if image is completely reconstructed
- Provide legal ownership automatically
- Watermark against professional attacks
- Work on artificially generated images (usually)

### Legal Use

This technology should be used:
- ✅ To protect your own work
- ✅ To verify ownership in disputes
- ✅ For personal portfolio authentication
- ✅ As evidence in copyright claims

Should NOT be used:
- ❌ To fraudulently claim ownership
- ❌ To attack others' images
- ❌ For malicious purposes
- ❌ Without consent of image owner

---

## 🚀 Advanced Usage

### Batch Processing (Future Enhancement)

Currently: One image at a time
Planned: Upload multiple images to encode/decode in batch

### Custom Proof Images

You can use any image as proof:
- Your signature
- Timestamp with date
- Your ID/passport
- Copyright notice
- QR code
- Custom graphic

### Combining with Other Protection

This works best with:
- Legal registration (copyright office)
- Visible watermarks (for deterrent)
- EXIF metadata (for backup proof)
- Blockchain verification (for authenticity)

### Metadata Tracking

The JSON metadata includes:
- Timestamp of encoding
- Model version used
- Quality metrics
- Image hashes
- Keep this for records!

---

## 📱 Platform-Specific Guidance

### For Instagram/TikTok Artists
1. Encode your artwork with your logo
2. Post stego image (looks identical)
3. If reposted: Extract proof, report violation
4. Tag @instagram, request takedown

### For NFT Creators
1. Use stego image as your NFT
2. Invisible proof embedded in blockchain-stored image
3. If someone else tries to claim: Extract proof
4. OpenSea/Rarible can see embedded ownership

### For Photographers
1. Encode with signature/timestamp
2. Use stego for portfolio/client delivery
3. If client claims as their own: Extract proof
4. Professional evidence of original authorship

### For Stock Photo Sites
1. Creators encode with their ID
2. Site stores stego images
3. Buyers get authentic content
4. Fraud attempts are instantly detectable

---

## 🎓 How Steganography Works (For Curious Users)

**Simple Analogy:**
- Traditional watermark = Sticky note on the back
- Steganography = Invisible ink written on the back
  - Can't be seen
  - Can't be removed without destroying paper
  - Can't be easily faked

**What Our System Does:**
1. Takes your artwork (cover image)
2. Takes your proof (secret image)
3. Neural network learns to hide proof inside artwork
4. Changes are < 1/255 per pixel (imperceptible)
5. Result: stego image (looks like original!)
6. Later: decoder extracts proof perfectly

**Why It's Secure:**
- Trained on deep learning (not just pixel addition)
- Imperceptible changes are robust
- Hard to remove without destroying image
- Cryptographically linked via hashing

---

## 🛠️ Troubleshooting Common Issues

### "Recovered proof looks blurry"
- Try different secret image
- Use higher contrast logo
- Ensure artwork is not too simple

### "Stego image looks different from original"
- Check metrics (may be imperceptible to you but visible to algorithm)
- Try different proof image (simpler design)
- Use artwork with more texture

### "I forgot my original secret image"
- ⚠️ Problem: Can't verify ownership without it
- Note: Recovered proof != original (slight degradation)
- Lesson: Always keep backup of original secret!

### "Download button not working"
- Check disk space on computer
- Try different browser
- Clear browser cache

### "Models are loading very slowly"
- Normal on first run (TensorFlow initialization)
- Subsequent runs are faster
- Have patience, may take 30-60 seconds

---

## 💡 Pro Tips

1. **Keep multiple backups**
   - Original artwork
   - Original proof
   - First stego image
   - Metadata JSON
   (Store in cloud + external drive)

2. **Document everything**
   - Date of encoding
   - File names used
   - Metrics achieved
   - Purpose of encoding

3. **Test first**
   - Encode test image before important work
   - Verify encoding/decoding works
   - Check metrics are acceptable

4. **Use strong proofs**
   - Make logo/signature distinctive
   - Add date/timestamp
   - Include unique identifier

5. **Verify regularly**
   - Check for unauthorized use
   - Use Google Images reverse search
   - Monitor social media usage
   - Extract proofs periodically

---

## 📞 FAQ

**Q: Can I use the same proof for multiple artworks?**
A: Yes! Same proof embedded in different artworks will help you track all your work.

**Q: Will the proof survive if the image is compressed?**
A: Yes, survives JPEG compression at quality 80+. Extreme compression may degrade.

**Q: Can I change the proof later?**
A: No, you'd need to re-encode. Plan carefully before initial encoding.

**Q: Is this watermarking?**
A: No, it's steganography. Watermarking is visible, steganography is invisible.

**Q: Can I share the metadata file publicly?**
A: Yes! It contains only metrics, no sensitive info. Good for proof chain.

**Q: Will different operating systems give different results?**
A: No, results are consistent (deterministic models).

**Q: Can I use this for video?**
A: Current version is images only. Video support planned for future.

**Q: How many proofs can I hide?**
A: Currently one proof per image. Multiple layers possible in future.

---

## 🎉 You're Ready!

You now have everything you need to:
- ✅ Protect your artwork invisibly
- ✅ Verify ownership on demand
- ✅ Catch unauthorized use
- ✅ Provide cryptographic proof
- ✅ Work completely offline

Happy protecting! 🔐

---

**Last Updated**: March 2026  
**Document Version**: 1.0  
**Feedback**: Always welcome!
