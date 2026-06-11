## 2026-04-06 - Replacing background-image with lazy-loaded <img> tags
**Learning:** Native `loading="lazy"` on semantic `<img>` tags provides significant performance improvements for below-the-fold content compared to CSS `background-image`, which lacks native lazy-loading support in most browsers. In this codebase, multiple below-the-fold images were being eagerly loaded due to the use of `background-image` within `div` elements, impacting initial page load time. Converting these to `<img loading="lazy">` reduces the initial payload and network requests on load. When verifying this via Playwright, remember headless browsers may still download them eagerly, so checking the HTML output directly is more reliable. Also, explicitly adding `object-cover w-full h-full` ensures the images replicate the `bg-cover bg-center` visual behavior precisely.

**Action:** Replace `div`s styled with `background-image` below the fold with `<img>` tags implementing `loading="lazy"`. Be careful to retain the existing classes, particularly sizing and layout (e.g. `object-cover object-center w-full h-full` instead of `bg-cover bg-center` if replacing the parent or using absolute inset).

## 2026-04-26 - Render Build Fallback
**Learning:** Render defaults to calling `npm run build` if the deployment environment is Node.js, even if `render.yaml` specifies a custom `buildCommand`. If a `package.json` file is present but lacks a `"build"` script, the deployment will fail immediately with "Empty build command; skipping build" and a missing publish directory error.
**Action:** When working with custom static build commands, always map them to a `"build"` script in `package.json` to ensure compatibility with PaaS defaults.

## 2026-05-15 - Preloading Responsive LCP Images
**Learning:** The browser's preload scanner cannot easily discover responsive image sources within a `<picture>` tag until it parses the DOM and evaluates the element. This delays the download of the Largest Contentful Paint (LCP) element.
**Action:** Always add a corresponding `<link rel="preload" as="image" imagesrcset="..." imagesizes="..." fetchpriority="high" />` to the HTML `<head>` for the LCP image. This makes the asset discoverable early by the preload scanner, avoiding waterfall delays and significantly improving the LCP metric.
