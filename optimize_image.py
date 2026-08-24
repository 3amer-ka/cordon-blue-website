from PIL import Image
import os

def optimize_image(input_path, output_dir, base_name="resort-design", widths=None, fallback_width=1920, fallback_suffix="-optimized"):
    try:
        img = Image.open(input_path)
    except Exception as e:
        print(f"Error opening image at {input_path}: {e}")
        return False

    if widths is None:
        widths = [640, 1280, 1920, 2560]

    cached_resized_images = {}

    for w in widths:
        h = int((w / img.width) * img.height)
        print(f"Resizing to {w}x{h}...")

        if (w, h) not in cached_resized_images:
            cached_resized_images[(w, h)] = img.resize((w, h), Image.Resampling.LANCZOS)

        resized = cached_resized_images[(w, h)]
        resized.save(os.path.join(output_dir, f'{base_name}-{w}w.webp'), 'WEBP', quality=80)

    # Fallback optimized jpeg
    if callable(fallback_width):
        w_fallback = fallback_width(img.width)
    else:
        w_fallback = fallback_width

    h_fallback = int((w_fallback / img.width) * img.height)

    if (w_fallback, h_fallback) in cached_resized_images:
        resized_jpg = cached_resized_images[(w_fallback, h_fallback)]
    else:
        resized_jpg = img.resize((w_fallback, h_fallback), Image.Resampling.LANCZOS)

    if resized_jpg.mode != 'RGB':
        resized_jpg = resized_jpg.convert('RGB')

    resized_jpg.save(os.path.join(output_dir, f'{base_name}{fallback_suffix}.jpg'), 'JPEG', quality=80)

    return True

if __name__ == '__main__':
    input_path = './assets/images/resort-design.jpg'
    output_dir = './assets/images/'
    optimize_image(input_path, output_dir)
