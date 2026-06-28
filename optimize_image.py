from PIL import Image
import os

def optimize_image(input_path, output_dir):
    try:
        img = Image.open(input_path)
    except Exception as e:
        print(f"Error: Could not open image at {input_path}. Reason: {e}")
        return False

    widths = [640, 1280, 1920, 2560]

    # Cache resized images to avoid redundant computation
    resized_cache = {}

    for w in widths:
        h = int((w / img.width) * img.height)
        print(f"Resizing to {w}x{h}...")
        resized = img.resize((w, h), Image.Resampling.LANCZOS)
        resized_cache[(w, h)] = resized
        resized.save(os.path.join(output_dir, f'resort-design-{w}w.webp'), 'WEBP', quality=80)

    # Fallback optimized jpeg
    h_fallback = int((1920 / img.width) * img.height)
    # Reuse cached image if available, avoiding an expensive resize
    if (1920, h_fallback) in resized_cache:
        resized_jpg = resized_cache[(1920, h_fallback)]
    else:
        resized_jpg = img.resize((1920, h_fallback), Image.Resampling.LANCZOS)

    # Ensure mode is RGB before saving as JPEG to prevent crashes
    if resized_jpg.mode != 'RGB':
        resized_jpg = resized_jpg.convert('RGB')

    resized_jpg.save(os.path.join(output_dir, 'resort-design-optimized.jpg'), 'JPEG', quality=80)

    return True

if __name__ == '__main__':
    input_path = './assets/images/resort-design.jpg'
    output_dir = './assets/images/'
    optimize_image(input_path, output_dir)
