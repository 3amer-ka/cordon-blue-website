from PIL import Image
import os

def optimize_image(input_path, output_dir):
    try:
        img = Image.open(input_path)
    except Exception as e:
        print(f"Error: Could not open image at {input_path}. {e}")
        return False

    widths = [640, 1280, 1920, 2560]

    # ⚡ Bolt Optimization: Cache intermediate resized Image objects
    # to avoid redundant .resize() computations for fallback images.
    resized_cache = {}

    for w in widths:
        h = int((w / img.width) * img.height)
        print(f"Resizing to {w}x{h}...")

        dim = (w, h)
        if dim not in resized_cache:
            resized_cache[dim] = img.resize(dim, Image.Resampling.LANCZOS)

        resized = resized_cache[dim]
        resized.save(os.path.join(output_dir, f'resort-design-{w}w.webp'), 'WEBP', quality=80)

    # Fallback optimized jpeg
    h_fallback = int((1920 / img.width) * img.height)
    dim_fallback = (1920, h_fallback)

    if dim_fallback in resized_cache:
        resized_jpg = resized_cache[dim_fallback]
    else:
        resized_jpg = img.resize(dim_fallback, Image.Resampling.LANCZOS)

    if resized_jpg.mode != 'RGB':
        resized_jpg = resized_jpg.convert('RGB')

    resized_jpg.save(os.path.join(output_dir, 'resort-design-optimized.jpg'), 'JPEG', quality=80)

    return True

if __name__ == '__main__':
    input_path = './assets/images/resort-design.jpg'
    output_dir = './assets/images/'
    optimize_image(input_path, output_dir)
