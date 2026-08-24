from optimize_image import optimize_image as base_optimize_image

def optimize_image(input_path, output_dir, base_name):
    return base_optimize_image(
        input_path=input_path,
        output_dir=output_dir,
        base_name=base_name,
        widths=[640, 1280],
        fallback_width=lambda w: min(w, 1280),
        fallback_suffix=''
    )

if __name__ == '__main__':
    input_path = './assets/images/hotel-resort-masterplan.jpg'
    output_dir = './assets/images/'
    base_name = 'hotel-resort-masterplan'
    optimize_image(input_path, output_dir, base_name)
