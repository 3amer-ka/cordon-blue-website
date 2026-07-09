from PIL import Image
import os

def optimize_image(input_path, output_dir):
    try:
        img = Image.open(input_path)
    except FileNotFoundError:
        print(f"Error: Image at {input_path} not found.")
        return False

    widths = [640, 1280, 1920, 2560]
    cached_resizes = {}

    for w in widths:
        h = int((w / img.width) * img.height)
        print(f"Resizing to {w}x{h}...")
        resized = img.resize((w, h), Image.Resampling.LANCZOS)
        cached_resizes[(w, h)] = resized
        resized.save(os.path.join(output_dir, f'resort-design-{w}w.webp'), 'WEBP', quality=80)

    # Fallback optimized jpeg
    h_fallback = int((1920 / img.width) * img.height)

    # Performance Optimization: Reuse the 1920px image from the cache if it was already generated in the loop above.
    # This avoids a redundant and expensive LANCZOS resize operation.
    if (1920, h_fallback) in cached_resizes:
        resized_jpg = cached_resizes[(1920, h_fallback)]
    else:
        resized_jpg = img.resize((1920, h_fallback), Image.Resampling.LANCZOS)

    resized_jpg.save(os.path.join(output_dir, 'resort-design-optimized.jpg'), 'JPEG', quality=80)

    return True

if __name__ == '__main__':
    input_path = './assets/images/resort-design.jpg'
    output_dir = './assets/images/'
    optimize_image(input_path, output_dir)
