#!/usr/bin/env python3
"""Test script to verify model loading without Streamlit cache issues"""

import os
import sys
from pathlib import Path

# Get script directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_ENCODER = os.path.join(SCRIPT_DIR, "unet_encoder_best.keras")
MODEL_DECODER = os.path.join(SCRIPT_DIR, "resnet_decoder_best.keras")

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
        from tensorflow.keras.models import load_model
        
        print("\n   Loading encoder model...")
        encoder = load_model(MODEL_ENCODER)
        print(f"   ✓ Encoder loaded successfully!")
        print(f"     └─ Input shapes: {[inp.shape for inp in encoder.inputs]}")
        # Handle both single and multiple outputs
        if isinstance(encoder.output, list):
            print(f"     └─ Output shapes: {[out.shape for out in encoder.output]}")
        else:
            print(f"     └─ Output shape: {encoder.output.shape}")
        print(f"     └─ Total layers: {len(encoder.layers)}")
        
        print("\n   Loading decoder model...")
        decoder = load_model(MODEL_DECODER)
        print(f"   ✓ Decoder loaded successfully!")
        # Handle both single and multiple inputs
        if isinstance(decoder.input, list):
            print(f"     └─ Input shapes: {[inp.shape for inp in decoder.input]}")
        else:
            print(f"     └─ Input shape: {decoder.input.shape}")
        # Handle both single and multiple outputs
        if isinstance(decoder.output, list):
            print(f"     └─ Output shapes: {[out.shape for out in decoder.output]}")
        else:
            print(f"     └─ Output shape: {decoder.output.shape}")
        print(f"     └─ Total layers: {len(decoder.layers)}")
        
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
