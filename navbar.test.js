const { JSDOM } = require('jsdom');
const fs = require('fs');
const assert = require('assert');
const path = require('path');

// Read the component code
const componentCode = fs.readFileSync(path.join(__dirname, 'navbar.js'), 'utf8');

// A helper function to create a fresh DOM and load the component
function setupDOM(url) {
    const dom = new JSDOM(`<!DOCTYPE html><html><body><main-header></main-header><main-footer></main-footer></body></html>`, {
        url: url,
        runScripts: "dangerously"
    });

    // Add the component code to the DOM
    const scriptEl = dom.window.document.createElement("script");
    scriptEl.textContent = componentCode;
    dom.window.document.body.appendChild(scriptEl);

    return dom;
}

async function runTests() {
    console.log("Running tests for MainHeader...");

    try {
        // Test 1: Home page active link
        let dom = setupDOM('http://localhost/index.html');
        let document = dom.window.document;
        let mainHeader = document.querySelector('main-header');

        let activeLinks = mainHeader.querySelectorAll('header nav a.text-primary');
        assert.strictEqual(activeLinks.length, 1, "There should be exactly 1 active link");
        assert.strictEqual(activeLinks[0].textContent.trim(), 'Home', "Active link should be Home");
        console.log("✅ Test 1 Passed: Home page active link");

        // Test 2: About page active link
        dom = setupDOM('http://localhost/about.html');
        document = dom.window.document;
        mainHeader = document.querySelector('main-header');

        activeLinks = mainHeader.querySelectorAll('header nav a.text-primary');
        assert.strictEqual(activeLinks.length, 1, "There should be exactly 1 active link");
        assert.strictEqual(activeLinks[0].textContent.trim(), 'About Us', "Active link should be About Us");
        console.log("✅ Test 2 Passed: About page active link");

        // Test 3: Mobile menu toggling
        dom = setupDOM('http://localhost/index.html');
        document = dom.window.document;
        mainHeader = document.querySelector('main-header');

        const button = mainHeader.querySelector('#mobile-menu-button');
        const menu = mainHeader.querySelector('#mobile-menu');

        // Initial state should have 'hidden' class
        assert.ok(menu.classList.contains('hidden'), "Menu should be hidden initially");

        // Click button to open
        button.click();
        assert.ok(!menu.classList.contains('hidden'), "Menu should not be hidden after click");

        // Click button to close
        button.click();
        assert.ok(menu.classList.contains('hidden'), "Menu should be hidden after second click");

        console.log("✅ Test 3 Passed: Mobile menu toggling");

        // Test 4: Mobile menu escape key closing
        // Open menu first
        button.click();
        assert.ok(!menu.classList.contains('hidden'), "Menu should not be hidden after click");

        // Simulate Escape key press
        const escapeEvent = new dom.window.KeyboardEvent('keydown', { key: 'Escape' });
        document.dispatchEvent(escapeEvent);

        assert.ok(menu.classList.contains('hidden'), "Menu should be hidden after pressing Escape");
        assert.strictEqual(button.getAttribute('aria-expanded'), 'false', "Aria-expanded should be false after closing");

        console.log("✅ Test 4 Passed: Mobile menu escape key closing");

        console.log("Running tests for MainFooter...");

        // Test 5: MainFooter container rendering
        let mainFooter = document.querySelector('main-footer');
        let footerElement = mainFooter.querySelector('footer');
        assert.ok(footerElement, "Footer container should be rendered");
        console.log("✅ Test 5 Passed: Footer container rendering");

        // Test 6: MainFooter logo source
        let logo = footerElement.querySelector('img[alt="Cordon Blue Global Services"]');
        assert.ok(logo, "Footer logo should be present");
        assert.strictEqual(logo.getAttribute('src'), './assets/images/logo_header.png', "Footer logo source should match");
        console.log("✅ Test 6 Passed: Footer logo source");

        // Test 7: MainFooter dynamic copyright year
        let currentYear = new Date().getFullYear();
        let copyrightText = footerElement.querySelector('.mt-16 p').textContent;
        assert.ok(copyrightText.includes(currentYear.toString()), "Copyright year should match the current year");
        console.log("✅ Test 7 Passed: Dynamic copyright year");

        // Test 8: MainFooter navigation links
        let quickLinks = footerElement.querySelectorAll('nav[aria-label="Quick Links"] a');
        let expectedLinks = ['Home', 'About Us', 'Our Services', 'Featured Projects'];
        assert.strictEqual(quickLinks.length, 4, "There should be exactly 4 quick links");
        for (let i = 0; i < expectedLinks.length; i++) {
            assert.strictEqual(quickLinks[i].textContent.trim(), expectedLinks[i], `Link ${i} should be ${expectedLinks[i]}`);
        }
        console.log("✅ Test 8 Passed: Navigation links");

        // Test 9: MainFooter contact information
        let contactInfo = footerElement.querySelector('address');
        assert.ok(contactInfo.textContent.includes('174, Ikorodu Road, Onipanu, Lagos, Nigeria'), "Address should be present");
        assert.ok(contactInfo.textContent.includes('+234 812 414 1514'), "Phone number should be present");
        assert.ok(contactInfo.textContent.includes('info@cordonblueglobal.com'), "Email should be present");
        console.log("✅ Test 9 Passed: Contact information accuracy");

    } catch (error) {

        console.error("❌ Test failed:", error);
        process.exit(1);
    }
}

runTests();
