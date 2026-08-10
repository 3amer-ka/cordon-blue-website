const { chromium } = require('playwright');
const path = require('path');

async function testFilter(page, filterName) {
  const filterButtons = page.locator('#project-filters button');
  const button = filterButtons.filter({ hasText: filterName });

  if (await button.count() > 0) {
    await button.click();
    console.log(`Clicked "${filterName}" filter.`);

    // Wait for the timeout (300ms) in projects.html to finish
    await page.waitForTimeout(400);

    const visibleCards = await page.$$eval('#project-grid > .group.flex.flex-col', cards => cards.filter(c => c.style.display !== 'none').length);
    console.log(`Visible cards after "${filterName}" filter: ${visibleCards}`);

    if (filterName !== 'All Projects') {
      const wrongCategoryCards = await page.$$eval('#project-grid > .group.flex.flex-col', (cards, filterName) => {
          return cards.filter(c => c.style.display !== 'none')
            .map(c => c.querySelector('.absolute.top-4.left-4 span')?.textContent.trim())
            .filter(cat => cat !== filterName);
      }, filterName);

      if (wrongCategoryCards.length > 0) {
        console.error(`Verification failed for "${filterName}". Found wrong categories: ${wrongCategoryCards.join(', ')}`);
      } else {
        console.log(`Verification passed: Only ${filterName} cards are visible.`);
      }
    }

    return visibleCards;
  } else {
    console.error(`Could not find ${filterName} filter button.`);
    return -1;
  }
}

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
  const filePath = path.resolve('projects.html');
  await page.goto(`file://${filePath}`, { waitUntil: 'domcontentloaded' });

  console.log('Page loaded successfully.');

  const initialCards = await page.$$eval('#project-grid > .group.flex.flex-col', cards => cards.filter(c => c.style.display !== 'none').length);
  console.log(`Initial visible cards: ${initialCards}`);

  const filterButtons = await page.$$eval('#project-filters button', btns => btns.map(b => b.textContent));
  console.log('Available filter buttons:', filterButtons);

  await testFilter(page, 'Hospitality');
  await testFilter(page, 'Commercial');

  const allVisibleCards = await testFilter(page, 'All Projects');

  if (allVisibleCards === initialCards) {
    console.log('Verification passed: All cards visible again.');
  } else {
    console.error(`Verification failed. Expected ${initialCards} cards, got ${allVisibleCards}.`);
  }

  await browser.close();
})();
