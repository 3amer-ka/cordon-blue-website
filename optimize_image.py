from PIL import Image
import os

def optimize_image(input_path, output_dir, base_name=None, widths=None, fallback_width=1920, fallback_suffix='-optimized'):
    try:
        img = Image.open(input_path)
    except FileNotFoundError:
        print(f"Error: Image at {input_path} not found.")
        return False

    widths = widths if widths is not None else [640, 1280, 1920, 2560]
    base_name = base_name if base_name is not None else os.path.splitext(os.path.basename(input_path))[0]

    for w in widths:
        h = int((w / img.width) * img.height)
        print(f"Resizing to {w}x{h}...")
        resized = img.resize((w, h), Image.Resampling.LANCZOS)
        resized.save(os.path.join(output_dir, f'{base_name}-{w}w.webp'), 'WEBP', quality=80)

    # Fallback optimized jpeg
    w_fallback = min(img.width, fallback_width)
    h_fallback = int((w_fallback / img.width) * img.height)
    resized_jpg = img.resize((w_fallback, h_fallback), Image.Resampling.LANCZOS)
    if img.mode != 'RGB':
        resized_jpg = resized_jpg.convert('RGB')
    resized_jpg.save(os.path.join(output_dir, f'{base_name}{fallback_suffix}.jpg'), 'JPEG', quality=80)

    return True

if __name__ == '__main__':
    # Optimize resort-design.jpg
    optimize_image('./assets/images/resort-design.jpg', './assets/images/')

    # Optimize hotel-resort-masterplan.jpg
    optimize_image(
        './assets/images/hotel-resort-masterplan.jpg',
        './assets/images/',
        widths=[640, 1280],
        fallback_width=1280,
        fallback_suffix=''
    )
