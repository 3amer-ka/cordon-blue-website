import { chromium } from 'playwright';

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1280, height: 720 }
});
const page = await context.newPage();

// Collect console messages
const consoleLogs = [];
page.on('console', msg => {
  if (msg.type() === 'error') {
    consoleLogs.push(`ERROR: ${msg.text()}`);
  }
});

// Collect page errors
const pageErrors = [];
page.on('pageerror', err => {
  pageErrors.push(err.message);
});

// Enable performance tracking
await page.goto('https://cordonblueglobal.com', { waitUntil: 'networkidle' });

// Get performance metrics
const metrics = await page.evaluate(() => {
  const timing = performance.getEntriesByType('navigation')[0];
  const paint = performance.getEntriesByType('paint');

  return {
    // Timing
    domContentLoaded: timing.domContentLoadedEventEnd - timing.startTime,
    loadComplete: timing.loadEventEnd - timing.startTime,
    firstPaint: paint.find(p => p.name === 'first-paint')?.startTime || 0,
    firstContentfulPaint: paint.find(p => p.name === 'first-contentful-paint')?.startTime || 0,
    largestContentfulPaint: 0, // Need more setup for this
    // Page info
    title: document.title,
    url: window.location.href,
    // Images
    images: Array.from(document.images).map(img => ({
      src: img.src,
      alt: img.alt,
      naturalWidth: img.naturalWidth,
      naturalHeight: img.naturalHeight,
      loading: img.loading,
      complete: img.complete
    }))
  };
});

console.log('=== Performance Analysis ===\n');
console.log(`Page: ${metrics.title}`);
console.log(`URL: ${metrics.url}\n`);

console.log('=== Timing Metrics (ms) ===');
console.log(`First Paint: ${Math.round(metrics.firstPaint)}ms`);
console.log(`First Contentful Paint: ${Math.round(metrics.firstContentfulPaint)}ms`);
console.log(`DOM Content Loaded: ${Math.round(metrics.domContentLoaded)}ms`);
console.log(`Page Load Complete: ${Math.round(metrics.loadComplete)}ms`);

console.log('\n=== Images ===');
metrics.images.forEach(img => {
  console.log(`\n[Image] ${img.src.split('/').pop()}`);
  console.log(`  Alt: "${img.alt}"`);
  console.log(`  Size: ${img.naturalWidth}x${img.naturalHeight}`);
  console.log(`  Loading: ${img.loading}`);
  console.log(`  Complete: ${img.complete}`);
});

// Get logo specifically
const logo = await page.locator('img[alt*="Logo"]').first();
const logoBox = await logo.boundingBox();
console.log(`\n=== Logo Element ===`);
console.log(`Logo found: ${await logo.count() > 0}`);
if (logoBox) {
  console.log(`Position: ${logoBox.x}, ${logoBox.y}`);
  console.log(`Size: ${logoBox.width}x${logoBox.height}`);
}

// Get all elements with background images
const bgImages = await page.evaluate(() => {
  const elements = document.querySelectorAll('[style*="background-image"]');
  return Array.from(elements).map(el => ({
    tag: el.tagName,
    classes: el.className,
    style: el.getAttribute('style'),
    rect: el.getBoundingClientRect()
  }));
});

console.log('\n=== Background Images ===');
bgImages.forEach(el => {
  const urlMatch = el.style.match(/url\("([^"]+)"\)/);
  if (urlMatch) {
    console.log(`[${el.tag}] ${el.classes}`);
    console.log(`  URL: ${urlMatch[1]}`);
    console.log(`  Size: ${el.rect.width}x${el.rect.height}`);
  }
});

// Resource loading
const resources = await page.evaluate(() => {
  const resources = performance.getEntriesByType('resource');
  return resources.map(r => ({
    name: r.name.split('/').pop(),
    type: r.initiatorType,
    size: r.transferSize,
    duration: r.duration
  })).filter(r => r.type === 'img' || r.type === 'link')
    .sort((a, b) => b.size - a.size)
    .slice(0, 10);
});

console.log('\n=== Top Resource Loads ===');
resources.forEach(r => {
  console.log(`${r.name}: ${(r.size/1024).toFixed(1)}KB (${Math.round(r.duration)}ms)`);
});

if (consoleLogs.length > 0) {
  console.log('\n=== Console Errors ===');
  consoleLogs.forEach(log => console.log(log));
}

if (pageErrors.length > 0) {
  console.log('\n=== Page Errors ===');
  pageErrors.forEach(err => console.log(err));
}

await browser.close();
