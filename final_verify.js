const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();

  await context.route('**/*', (route) => {
    const url = route.request().url();
    if (url.includes('cdn.tailwindcss.com') || url.includes('fonts.googleapis') || url.includes('fonts.gstatic')) {
      return route.abort();
    }
    return route.continue();
  });

  const page = await context.newPage();

  // Setup dialog handler to catch the JS alerts we added
  let dialogMessages = [];
  page.on('dialog', async dialog => {
    dialogMessages.push(dialog.message());
    await dialog.accept();
  });

  const filePath = path.resolve('projects.html');
  await page.goto(`file://${filePath}`, { waitUntil: 'domcontentloaded' });

  // 1. Verify links
  console.log('Verifying links...');
  const aHrefs = await page.$$eval('a', anchors => anchors.map(a => a.getAttribute('href')));
  const duplicateHrefs = aHrefs.filter(href => href && href.includes(' href='));
  if (duplicateHrefs.length > 0) {
    console.error('FAILED: Found links with duplicate hrefs:', duplicateHrefs);
  } else {
    console.log('PASSED: No duplicate hrefs found in links.');
  }

  // 2. Verify specific image change
  console.log('Verifying image change...');
  const hotelCard = await page.locator('#project-grid > .group.flex.flex-col').filter({ hasText: 'Hotel & Resort Masterplan' });
  if (await hotelCard.count() > 0) {
    const bgImage = await hotelCard.locator('.bg-cover').evaluate(node => node.style.backgroundImage);
    if (bgImage.includes('resort-design.jpg')) {
      console.log('PASSED: Correct background image applied to Hotel & Resort Masterplan card.');
    } else {
      console.error(`FAILED: Incorrect background image. Expected resort-design.jpg, got ${bgImage}`);
    }
  } else {
    console.error('FAILED: Could not find "Hotel & Resort Masterplan" card.');
  }

  // 3. Verify alerts on buttons
  console.log('Verifying button interactivity...');

  // Contact Button
  const contactBtn = page.locator('button').filter({ hasText: 'Contact Us Today' });
  if (await contactBtn.count() > 0) {
    await contactBtn.click();
    await page.waitForTimeout(100);
    if (dialogMessages.includes('Contact action triggered')) {
      console.log('PASSED: Contact button triggers alert.');
    } else {
      console.error('FAILED: Contact button did not trigger alert.');
    }
  } else {
    console.error('FAILED: Could not find Contact button.');
  }

  // Download Button
  const downloadBtn = page.locator('button').filter({ hasText: 'Download Brochure' });
  if (await downloadBtn.count() > 0) {
    await downloadBtn.click();
    await page.waitForTimeout(100);
    if (dialogMessages.includes('Download action triggered')) {
      console.log('PASSED: Download button triggers alert.');
    } else {
      console.error('FAILED: Download button did not trigger alert.');
    }
  } else {
    console.error('FAILED: Could not find Download button.');
  }

  await browser.close();
})();
