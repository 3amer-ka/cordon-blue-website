import re

def optimize_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    def replacer(match):
        classes = match.group(1)
        data_alt_full = match.group(2)
        alt_text = match.group(3) if match.group(3) else "Project image"
        url = match.group(4)

        new_classes = classes.replace('bg-cover', 'object-cover w-full h-full').replace('bg-center', 'object-center').replace('bg-no-repeat', '')

        class_list = []
        for c in new_classes.split():
            if c not in class_list:
                class_list.append(c)
        new_classes = " ".join(class_list)

        return f'<!-- ⚡ Bolt: Replaced background-image with lazy-loaded img tag for performance -->\n<img src="{url}" alt="{alt_text}" class="{new_classes}" loading="lazy">'

    pattern = re.compile(r'<div class="([^"]*?)"\s*(data-alt="([^"]*?)")?\s*style=[\'"]background-image:\s*url\([\'"]([^\'"]*?)[\'"]\);?[\'"]></div>')

    new_content = pattern.sub(replacer, content)

    with open(filename, 'w') as f:
        f.write(new_content)

optimize_file('index.html')
optimize_file('projects.html')
optimize_file('services.html')
