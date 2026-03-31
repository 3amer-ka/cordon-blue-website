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
  const filePath = path.resolve('projects.html');
  await page.goto(`file://${filePath}`, { waitUntil: 'domcontentloaded' });

  console.log('Page loaded successfully.');

  const filterButtons = await page.$$eval('#project-filters button', btns => btns.map(b => b.textContent));
  console.log('Filter buttons:', filterButtons);

  // Since 'Hospitality' is not a button, let's use 'Commercial'
  const commercialButton = page.locator('#project-filters button').filter({ hasText: 'Commercial' });

  if (await commercialButton.count() > 0) {
    await commercialButton.click();
    console.log('Clicked "Commercial" filter.');

    await page.waitForTimeout(100);

    const visibleCardsCount = await page.$$eval('#project-grid > .group.flex.flex-col', cards => cards.filter(c => c.style.display !== 'none').length);
    console.log(`Visible cards after filter: ${visibleCardsCount}`);

    const visibleCardCategories = await page.$$eval('#project-grid > .group.flex.flex-col', cards => {
        return cards.filter(c => c.style.display !== 'none').map(c => c.querySelector('.absolute.top-4.left-4 span')?.textContent.trim());
    });
    console.log(`Visible categories: ${visibleCardCategories.join(', ')}`);
  } else {
    console.error('Could not find Commercial filter button.');
  }

  await browser.close();
})();
