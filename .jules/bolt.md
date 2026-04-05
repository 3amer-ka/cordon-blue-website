## 2026-04-05 - Lazy Loading Verification with Playwright
**Learning:** When verifying `loading="lazy"` optimizations via Playwright headless browser, the browser may still eagerly download all images regardless of viewport settings.
**Action:** Do not rely solely on network request intercepts in Playwright to prove lazy loading works. Instead, validate the presence of the HTML attribute and visual layout, or test manually.

## 2026-04-05 - Over-eager Lazy Loading
**Learning:** Applying `loading="lazy"` to images above the fold is a performance anti-pattern as it delays Largest Contentful Paint (LCP) because the browser waits for layout calculation before fetching the image.
**Action:** Only apply `loading="lazy"` to images explicitly guaranteed to be below the fold on initial render.
