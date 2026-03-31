from PIL import Image
import os
import time

input_path = './assets/images/resort-design.jpg'
output_dir = './assets/images/'

img = Image.open(input_path)
widths = [640, 1280, 1920, 2560]

for w in widths:
    h = int((w / img.width) * img.height)
    print(f"Resizing to {w}x{h}...")
    resized = img.resize((w, h), Image.Resampling.LANCZOS)
    resized.save(os.path.join(output_dir, f'resort-design-{w}w.webp'), 'WEBP', quality=80)

# Fallback optimized jpeg
h_fallback = int((1920 / img.width) * img.height)
resized_jpg = img.resize((1920, h_fallback), Image.Resampling.LANCZOS)
resized_jpg.save(os.path.join(output_dir, 'resort-design-optimized.jpg'), 'JPEG', quality=80)
