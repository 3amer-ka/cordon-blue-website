from playwright.sync_api import sync_playwright
import os

# Use current directory for verification output
VERIFICATION_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "verification")
os.makedirs(os.path.join(VERIFICATION_DIR, "videos"), exist_ok=True)
os.makedirs(os.path.join(VERIFICATION_DIR, "screenshots"), exist_ok=True)

def run_cuj(page, url, name):
    page.goto(url, wait_until='domcontentloaded')
    page.wait_for_timeout(1000)
    page.screenshot(path=os.path.join(VERIFICATION_DIR, "screenshots", f"{name}.png"))
    page.wait_for_timeout(500)

def block_external_resources(route):
    if not any(x in route.request.url for x in ["fonts.googleapis.com", "cdn.tailwindcss.com"]):
        route.continue_()
    else:
        route.abort()

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir=os.path.join(VERIFICATION_DIR, "videos")
        )

        # Block external resources to avoid timeouts
        context.route("**/*", block_external_resources)

        page = context.new_page()
        try:
            run_cuj(page, "http://localhost:3000/index.html", "index")
            run_cuj(page, "http://localhost:3000/projects.html", "projects")
            run_cuj(page, "http://localhost:3000/services.html", "services")
        finally:
            context.close()
            browser.close()

if __name__ == "__main__":
    main()
