const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();

  // To avoid Playwright timeouts during frontend verification in this environment,
  // block external network requests (e.g., fonts.googleapis.com, cdn.tailwindcss.com)
  await context.route('**/*', (route) => {
    const url = route.request().url();
    if (url.includes('cdn.tailwindcss.com') || url.includes('fonts.googleapis') || url.includes('fonts.gstatic')) {
      return route.abort();
    }
    return route.continue();
  });

  const page = await context.newPage();
  const filePath = path.resolve('projects.html');
  await page.goto(`file://${filePath}`, { waitUntil: 'domcontentloaded' });

  console.log('Page loaded successfully.');

  // Check initial state
  const initialCards = await page.$$eval('#project-grid > .group.flex.flex-col', cards => cards.filter(c => c.style.display !== 'none').length);
  console.log(`Initial visible cards: ${initialCards}`);

  // Click 'Hospitality' filter button
  const filterButtons = page.locator('#project-filters button');
  const hospitalityButton = filterButtons.filter({ hasText: 'Hospitality' });

  if (await hospitalityButton.count() > 0) {
    await hospitalityButton.click();
    console.log('Clicked "Hospitality" filter.');

    // Wait for the animation to finish
    await page.waitForTimeout(400);

    // Check visible cards
    const visibleCards = await page.$$eval('#project-grid > .group.flex.flex-col', cards => cards.filter(c => c.style.display !== 'none').length);
    console.log(`Visible cards after filter: ${visibleCards}`);

    // Verify all visible cards are 'Hospitality'
    const wrongCategoryCards = await page.$$eval('#project-grid > .group.flex.flex-col', cards => {
        return cards.filter(c => c.style.display !== 'none').map(c => c.querySelector('.absolute.top-4.left-4 span')?.textContent.trim()).filter(cat => cat !== 'Hospitality');
    });

    if (wrongCategoryCards.length > 0) {
      console.error(`Verification failed. Found wrong categories: ${wrongCategoryCards.join(', ')}`);
    } else {
      console.log('Verification passed: Only Hospitality cards are visible.');
    }
  } else {
    console.error('Could not find Hospitality filter button.');
  }

  // Click 'All Projects' filter button
  const allButton = filterButtons.filter({ hasText: 'All Projects' });
  if (await allButton.count() > 0) {
    await allButton.click();
    console.log('Clicked "All Projects" filter.');
    await page.waitForTimeout(400);
    const allVisibleCards = await page.$$eval('#project-grid > .group.flex.flex-col', cards => cards.filter(c => c.style.display !== 'none').length);
    console.log(`Visible cards after 'All Projects' filter: ${allVisibleCards}`);

    if (allVisibleCards === initialCards) {
      console.log('Verification passed: All cards visible again.');
    } else {
      console.error(`Verification failed. Expected ${initialCards} cards, got ${allVisibleCards}.`);
    }
  }

  await browser.close();
})();
