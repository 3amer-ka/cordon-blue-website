from PIL import Image
import os

def optimize_image(input_path, output_dir, base_name):
    try:
        img = Image.open(input_path)
    except Exception as e:
        print(f"Error: Could not open image at {input_path}: {e}")
        return False

    widths = [640, 1280]
    # ⚡ Bolt Optimization: Cache intermediate resized Image objects
    # This avoids redundantly computing .resize() for the fallback JPEG
    resized_cache = {}

    for w in widths:
        h = int((w / img.width) * img.height)
        print(f"Resizing to {w}x{h}...")
        resized = img.resize((w, h), Image.Resampling.LANCZOS)
        resized_cache[(w, h)] = resized
        resized.save(os.path.join(output_dir, f'{base_name}-{w}w.webp'), 'WEBP', quality=80)

    # Fallback optimized jpeg
    # We will just save it optimized with its original size or max 1280 width to save space
    w_fallback = min(img.width, 1280)
    h_fallback = int((w_fallback / img.width) * img.height)
    # ⚡ Bolt Optimization: Retrieve cached resized image instead of re-resizing
    if (w_fallback, h_fallback) in resized_cache:
        resized_jpg = resized_cache[(w_fallback, h_fallback)]
    else:
        resized_jpg = img.resize((w_fallback, h_fallback), Image.Resampling.LANCZOS)

    if resized_jpg.mode != 'RGB':
        resized_jpg = resized_jpg.convert('RGB')

    resized_jpg.save(os.path.join(output_dir, f'{base_name}.jpg'), 'JPEG', quality=80)

    return True

if __name__ == '__main__':
    input_path = './assets/images/hotel-resort-masterplan.jpg'
    output_dir = './assets/images/'
    base_name = 'hotel-resort-masterplan'
    optimize_image(input_path, output_dir, base_name)
