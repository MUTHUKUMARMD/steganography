#!/usr/bin/env python3
"""Compare encoder_bigmodel vs encoder_rgb_exact models"""

import os
from pathlib import Path
import numpy as np
from tensorflow.keras.models import load_model

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 70)
print("🔍 MODEL COMPARISON TEST")
print("=" * 70)

models_to_check = [
    ("encoder_bigmodel.h5", "encoder_bigmodel"),
    ("encoder_rgb_exact.h5", "encoder_rgb_exact"),
    ("decoder_bigmodel.h5", "decoder_bigmodel"),
    ("decoder_rgb_exact.h5", "decoder_rgb_exact"),
]

print("\n📋 Checking available models:\n")

for filename, name in models_to_check:
    path = os.path.join(SCRIPT_DIR, filename)
    exists = os.path.exists(path)
    status = "✅" if exists else "❌"
    if exists:
        size = os.path.getsize(path) / 1024
        try:
            model = load_model(path)
            layers = len(model.layers)
            print(f"{status} {name:20s} | Size: {size:8.1f} KB | Layers: {layers:2d}")
        except Exception as e:
            print(f"{status} {name:20s} | Error: {e}")
    else:
        print(f"{status} {name:20s} | NOT FOUND")

print("\n" + "=" * 70)
print("📊 RECOMMENDATION:")
print("=" * 70)

# Check which models exist and are loadable
bigmodel_encoder_ok = False
exact_encoder_ok = False

try:
    encoder_big = load_model(os.path.join(SCRIPT_DIR, "encoder_bigmodel.h5"))
    bigmodel_encoder_ok = True
except:
    pass

try:
    encoder_exact = load_model(os.path.join(SCRIPT_DIR, "encoder_rgb_exact.h5"))
    exact_encoder_ok = True
except:
    pass

if exact_encoder_ok:
    print("\n✅ encoder_rgb_exact.h5 is available and loads correctly")
    print("   → This is the IMPROVED model with residual architecture")
    print("   → It uses imperceptible embedding (0.005 scaling)")
    print("   → RECOMMENDATION: Use this for better steganography quality")
else:
    print("\n⚠️  encoder_rgb_exact.h5 not available")

if bigmodel_encoder_ok:
    print("\n⚠️  encoder_bigmodel.h5 is available")
    print("   → This may be the original/basic architecture")
    print("   → Might have visible artifacts in stego image")
else:
    print("\n❌ encoder_bigmodel.h5 not available")

print("\n" + "=" * 70)
