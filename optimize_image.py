from PIL import Image
import os

def optimize_image(input_path, output_dir):
    try:
        img = Image.open(input_path)
    except Exception as e:
        print(f"Error: Image at {input_path} could not be opened. {e}")
        return False

    widths = [640, 1280, 1920, 2560]

    # ⚡ Bolt Optimization: Cache intermediate resized objects
    resized_cache = {}

    for w in widths:
        h = int((w / img.width) * img.height)
        print(f"Resizing to {w}x{h}...")
        resized = img.resize((w, h), Image.Resampling.LANCZOS)
        resized_cache[w] = resized
        resized.save(os.path.join(output_dir, f'resort-design-{w}w.webp'), 'WEBP', quality=80)

    # Fallback optimized jpeg
    w_fallback = 1920
    h_fallback = int((w_fallback / img.width) * img.height)

    # Use cached image if available to avoid redundant resize computation
    if w_fallback in resized_cache:
        resized_jpg = resized_cache[w_fallback].copy()
    else:
        resized_jpg = img.resize((w_fallback, h_fallback), Image.Resampling.LANCZOS)

    if resized_jpg.mode != 'RGB':
        resized_jpg = resized_jpg.convert('RGB')

    resized_jpg.save(os.path.join(output_dir, 'resort-design-optimized.jpg'), 'JPEG', quality=80)

    return True

if __name__ == '__main__':
    input_path = './assets/images/resort-design.jpg'
    output_dir = './assets/images/'
    optimize_image(input_path, output_dir)
