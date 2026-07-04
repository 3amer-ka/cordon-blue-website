from PIL import Image
import os

def optimize_image(input_path, output_dir):
    try:
        img = Image.open(input_path)
    except Exception as e:
        print(f"Error opening image at {input_path}: {e}")
        return False

    widths = [640, 1280, 1920, 2560]

    # Cache intermediate resized images keyed by dimension to avoid redundant computations
    resize_cache = {}

    for w in widths:
        h = int((w / img.width) * img.height)

        # Check cache before resizing
        if (w, h) in resize_cache:
            resized = resize_cache[(w, h)]
        else:
            print(f"Resizing to {w}x{h}...")
            resized = img.resize((w, h), Image.Resampling.LANCZOS)
            resize_cache[(w, h)] = resized

        resized.save(os.path.join(output_dir, f'resort-design-{w}w.webp'), 'WEBP', quality=80)

    # Fallback optimized jpeg
    h_fallback = int((1920 / img.width) * img.height)
    if (1920, h_fallback) in resize_cache:
        resized_jpg = resize_cache[(1920, h_fallback)]
    else:
        resized_jpg = img.resize((1920, h_fallback), Image.Resampling.LANCZOS)

    # Convert non-RGB mode to RGB before saving as JPEG to prevent crashes
    if resized_jpg.mode != 'RGB':
        resized_jpg = resized_jpg.convert('RGB')

    resized_jpg.save(os.path.join(output_dir, 'resort-design-optimized.jpg'), 'JPEG', quality=80)

    return True

if __name__ == '__main__':
    input_path = './assets/images/resort-design.jpg'
    output_dir = './assets/images/'
    optimize_image(input_path, output_dir)
