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

    # Find the header section to restrict search
    header_match = re.search(r'<header.*?</header>', content, re.DOTALL)
    if not header_match:
        print(f"Could not find header in {filepath}")
        continue
    header_content = header_match.group(0)

    # We want to replace the FIRST <div class="flex items-center gap-3"> ... </div>
    # Let's match it precisely

    if filepath == "projects.html":
        old_div = re.search(r'<div class="flex items-center gap-3">\s*<div class="size-10 bg-primary.*?</div>\s*</div>', header_content, re.DOTALL)
    else:
        old_div = re.search(r'<div class="flex items-center gap-3">\s*<div class="flex items-center justify-center bg-primary.*?</div>\s*<span class="text-xl font-bold tracking-tight text-slate-900 dark:text-white uppercase">Cordon Blue Global Services Ltd.</span>\s*</div>', header_content, re.DOTALL)

    if old_div:
        new_header_content = header_content.replace(old_div.group(0), new_header)
        content = content.replace(header_content, new_header_content)

        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Successfully updated {filepath}")
    else:
        print(f"Could not find matching div in {filepath}")
