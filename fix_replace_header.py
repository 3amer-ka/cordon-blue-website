import re

files = ["index.html", "projects.html", "services.html"]

new_header = """<div class="flex items-center gap-3">
<div class="size-12 bg-white rounded-2xl flex items-center justify-center overflow-hidden shrink-0 shadow-sm border border-slate-200/50">
<img alt="Cordon Blue Logo" class="w-full h-full object-cover p-1" src="./assets/logo.jpg"/>
</div>
<div class="flex flex-col">
<h2 class="text-xl md:text-2xl font-black leading-tight tracking-tight text-slate-900 dark:text-white">Cordon Blue</h2>
<p class="text-[13px] md:text-sm text-slate-500 dark:text-slate-400 font-semibold leading-tight mt-0.5">Global Services Ltd.</p>
</div>
</div>"""

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    if filepath == "projects.html":
        # Look for the specific part to replace in projects.html
        old_div_match = re.search(r'(<div class="flex items-center gap-3">\s*<div class="size-10 bg-primary rounded-lg flex items-center justify-center text-white">\s*<img[^>]*>\s*</div>\s*<div>\s*<h2[^>]*>Cordon Blue Global Services Ltd\.</h2>\s*<p[^>]*>Global Services Ltd\.</p>\s*</div>\s*</div>)', content, re.DOTALL)
    else:
        # Look for the specific part to replace in index.html and services.html
        old_div_match = re.search(r'(<div class="flex items-center gap-3">\s*<div class="flex items-center justify-center bg-primary.*?</div>\s*<span class="text-xl font-bold tracking-tight text-slate-900 dark:text-white uppercase">Cordon Blue Global Services Ltd\.</span>\s*</div>)', content, re.DOTALL)

    if old_div_match:
        content = content.replace(old_div_match.group(1), new_header)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Successfully updated {filepath}")
    else:
        print(f"Could not find matching div in {filepath}")
