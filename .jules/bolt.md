## 2024-04-03 - Lazy loading background images
**Learning:** Background images loaded via inline styles (e.g. `style="background-image: url(...)"`) are parsed and downloaded eagerly by the browser, blocking initial render.
**Action:** Replace background images that are below the fold with native semantic `<img>` tags utilizing the `loading="lazy"` attribute, reducing initial page load weight and improving time to interactive.
