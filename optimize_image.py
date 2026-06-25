from PIL import Image
import os

def optimize_image(input_path, output_dir):
    try:
        img = Image.open(input_path)
    except Exception as e:
        print(f"Error: Could not open image at {input_path}. Reason: {e}")
        return False

    widths = [640, 1280, 1920, 2560]

    # ⚡ Bolt Optimization: Cache resized Image objects
    # Avoids redundant resize operations if the fallback image shares the same dimensions.
    cache = {}

    for w in widths:
        h = int((w / img.width) * img.height)
        print(f"Resizing to {w}x{h}...")
        resized = img.resize((w, h), Image.Resampling.LANCZOS)
        cache[(w, h)] = resized
        resized.save(os.path.join(output_dir, f'resort-design-{w}w.webp'), 'WEBP', quality=80)

    # Fallback optimized jpeg
    h_fallback = int((1920 / img.width) * img.height)

    # Check if we already have the 1920 fallback in cache
    if (1920, h_fallback) in cache:
        resized_jpg = cache[(1920, h_fallback)]
    else:
        resized_jpg = img.resize((1920, h_fallback), Image.Resampling.LANCZOS)

    resized_jpg.save(os.path.join(output_dir, 'resort-design-optimized.jpg'), 'JPEG', quality=80)

    return True

if __name__ == '__main__':
    input_path = './assets/images/resort-design.jpg'
    output_dir = './assets/images/'
    optimize_image(input_path, output_dir)
