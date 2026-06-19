from PIL import Image
import os

def optimize_image(input_path, output_dir):
    try:
        img = Image.open(input_path)
    except Exception as e:
        print(f"Error opening image at {input_path}: {e}")
        return False

    widths = [640, 1280, 1920, 2560]

    # ⚡ Bolt Optimization: Cache resized images by their dimensions
    # to avoid redundant `.resize()` computations for fallback images.
    cache = {}

    for w in widths:
        h = int((w / img.width) * img.height)
        print(f"Resizing to {w}x{h}...")
        if (w, h) not in cache:
            cache[(w, h)] = img.resize((w, h), Image.Resampling.LANCZOS)
        resized = cache[(w, h)]
        resized.save(os.path.join(output_dir, f'resort-design-{w}w.webp'), 'WEBP', quality=80)

    # Fallback optimized jpeg
    h_fallback = int((1920 / img.width) * img.height)
    if (1920, h_fallback) not in cache:
        cache[(1920, h_fallback)] = img.resize((1920, h_fallback), Image.Resampling.LANCZOS)
    resized_jpg = cache[(1920, h_fallback)]
    resized_jpg.save(os.path.join(output_dir, 'resort-design-optimized.jpg'), 'JPEG', quality=80)

    return True

if __name__ == '__main__':
    input_path = './assets/images/resort-design.jpg'
    output_dir = './assets/images/'
    optimize_image(input_path, output_dir)
