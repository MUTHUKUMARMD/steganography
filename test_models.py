#!/usr/bin/env python3
"""Test script to verify model loading without Streamlit cache issues"""

import os
import sys
from pathlib import Path

# Get script directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_ENCODER = os.path.join(SCRIPT_DIR, "encoder_rgb_exact.h5")
MODEL_DECODER = os.path.join(SCRIPT_DIR, "decoder_rgb_exact.h5")

print("=" * 70)
print("🔐 INVISIBLE DRM - MODEL DIAGNOSTIC TEST")
print("=" * 70)

print(f"\n📍 Script Directory: {SCRIPT_DIR}")
print(f"\n📁 Checking for model files:")
print(f"   Encoder: {MODEL_ENCODER}")
print(f"   └─ Exists: {os.path.exists(MODEL_ENCODER)}")
if os.path.exists(MODEL_ENCODER):
    size = os.path.getsize(MODEL_ENCODER) / 1024
    print(f"   └─ Size: {size:.1f} KB")

print(f"\n   Decoder: {MODEL_DECODER}")
print(f"   └─ Exists: {os.path.exists(MODEL_DECODER)}")
if os.path.exists(MODEL_DECODER):
    size = os.path.getsize(MODEL_DECODER) / 1024
    print(f"   └─ Size: {size:.1f} KB")

print(f"\n" + "=" * 70)

if os.path.exists(MODEL_ENCODER) and os.path.exists(MODEL_DECODER):
    print("\n✅ Both model weight files found! Building architectures and loading weights...")
    
    try:
        from tensorflow.keras.models import Model
        from tensorflow.keras.layers import Input, Conv2D, GaussianNoise, Concatenate
        
        def build_encoder_model(img_size=128):
            """Build encoder model architecture"""
            s = Input((img_size, img_size, 3), name='secret_rgb')
            c = Input((img_size, img_size, 3), name='cover_rgb')
            x = Concatenate(axis=-1)([c, s])  # 6 channels
            x = Conv2D(64, 3, padding='same', activation='relu')(x)
            x = Conv2D(64, 3, padding='same', activation='relu')(x)
            x = Conv2D(32, 3, padding='same', activation='relu')(x)
            stego = Conv2D(3, 3, padding='same', activation='sigmoid', name='stego_rgb')(x)
            return Model([s, c], stego, name='encoder')
        
        def build_decoder_model(img_size=128):
            """Build decoder model architecture"""
            inp = Input((img_size, img_size, 3), name='stego_input')
            x = GaussianNoise(0.01)(inp)
            x1 = Conv2D(64, 3, padding='same', activation='relu')(x)
            x2 = Conv2D(32, 3, padding='same', activation='relu')(x)
            x = Concatenate(axis=-1)([x1, x2])
            x = Conv2D(64, 3, padding='same', activation='relu')(x)
            x = Conv2D(32, 3, padding='same', activation='relu')(x)
            recovered = Conv2D(3, 3, padding='same', activation='sigmoid', name='recovered_rgb')(x)
            return Model(inp, recovered, name='decoder')
        
        print("\n   Building encoder architecture...")
        encoder = build_encoder_model(128)
        print(f"   ✓ Encoder architecture built")
        
        print("   Loading encoder weights...")
        encoder.load_weights(MODEL_ENCODER)
        print(f"   ✓ Encoder weights loaded successfully!")
        print(f"     └─ Input shapes: {[inp.shape for inp in encoder.inputs]}")
        print(f"     └─ Output shape: {encoder.output.shape}")
        
        print("\n   Building decoder architecture...")
        decoder = build_decoder_model(128)
        print(f"   ✓ Decoder architecture built")
        
        print("   Loading decoder weights...")
        decoder.load_weights(MODEL_DECODER)
        print(f"   ✓ Decoder weights loaded successfully!")
        print(f"     └─ Input shape: {decoder.input.shape}")
        print(f"     └─ Output shape: {decoder.output.shape}")
        
        print("\n" + "=" * 70)
        print("✅ SUCCESS! Models are ready to use with Streamlit")
        print("=" * 70)
        sys.exit(0)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("\nStack trace:")
        import traceback
        traceback.print_exc()
        sys.exit(1)
else:
    print("\n❌ ERROR: Models not found in the expected location!")
    print("\nExpected location (same directory as this script):")
    print(f"   {SCRIPT_DIR}")
    
    print("\nFiles in this directory:")
    files = os.listdir(SCRIPT_DIR)
    for f in sorted(files):
        if not f.startswith('.'):
            full_path = os.path.join(SCRIPT_DIR, f)
            if os.path.isdir(full_path):
                print(f"   📁 {f}/")
            else:
                size = os.path.getsize(full_path) / 1024
                print(f"   📄 {f} ({size:.1f} KB)")
    
    sys.exit(1)
