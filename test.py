import re

content = """
<header class="sticky top-0 z-50 w-full border-b border-slate-200/60 dark:border-white/5 bg-background-light/80 dark:bg-background-dark/80 backdrop-blur-xl">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
<div class="flex h-20 items-center justify-between">
<div class="flex items-center gap-3">
<div class="flex items-center justify-center bg-primary p-2 rounded-xl shadow-lg shadow-primary/20">
<span class="material-symbols-outlined text-white text-2xl">architecture</span>
</div>
<span class="text-xl font-bold tracking-tight text-slate-900 dark:text-white uppercase">Cordon Blue Global Services Ltd.</span>
</div>
"""

old_div = re.search(r'<div class="flex items-center gap-3">.*?<span class="text-xl font-bold tracking-tight text-slate-900 dark:text-white uppercase">Cordon Blue Global Services Ltd\.</span>\s*</div>', content, re.DOTALL)
if old_div:
    print("MATCH!")
else:
    print("NO MATCH")
