const { JSDOM } = require('jsdom');
const fs = require('fs');
const assert = require('assert');
const path = require('path');

// Read the component code
const componentCode = fs.readFileSync(path.join(__dirname, 'navbar.js'), 'utf8');

// A helper function to create a fresh DOM and load the component
function setupDOM(url) {
    const dom = new JSDOM(`<!DOCTYPE html><html><body><main-header></main-header></body></html>`, {
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

        let activeLinks = mainHeader.querySelectorAll('header > div > nav a.text-primary');
        assert.strictEqual(activeLinks.length, 1, "There should be exactly 1 active link");
        assert.strictEqual(activeLinks[0].textContent.trim(), 'Home', "Active link should be Home");
        console.log("✅ Test 1 Passed: Home page active link");

        // Test 2: About page active link
        dom = setupDOM('http://localhost/about.html');
        document = dom.window.document;
        mainHeader = document.querySelector('main-header');

        activeLinks = mainHeader.querySelectorAll('header > div > nav a.text-primary');
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

    } catch (error) {
        console.error("❌ Test failed:", error);
        process.exit(1);
    }
}

runTests();
