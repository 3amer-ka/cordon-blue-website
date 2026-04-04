## 2026-04-04 - [Replaced elements vs Background Image]
**Learning:** [When migrating divs with CSS background images and `inset-0` (top:0, left:0, bottom:0, right:0) to <img> tags, the <img> will default to intrinsic image sizes rather than stretching like a div because it is a "replaced element". Also avoid lazily loading above-the-fold images to avoid LCP performance regression.]
**Action:** [Always include `w-full h-full` explicitly on replaced elements and check if the element is above-the-fold before adding `loading="lazy"`]
