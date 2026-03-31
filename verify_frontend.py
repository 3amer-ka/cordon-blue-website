from playwright.sync_api import sync_playwright
import os

os.makedirs("/home/jules/verification/videos", exist_ok=True)
os.makedirs("/home/jules/verification/screenshots", exist_ok=True)

def run_cuj(page, url, name):
    page.goto(url, wait_until='domcontentloaded')
    page.wait_for_timeout(1000)
    page.screenshot(path=f"/home/jules/verification/screenshots/{name}.png")
    page.wait_for_timeout(500)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )

        # Block external resources to avoid timeouts
        context.route("**/*", lambda route: route.continue_() if not any(x in route.request.url for x in ["fonts.googleapis.com", "cdn.tailwindcss.com"]) else route.abort())

        page = context.new_page()
        try:
            run_cuj(page, "http://localhost:3000/index.html", "index")
            run_cuj(page, "http://localhost:3000/projects.html", "projects")
            run_cuj(page, "http://localhost:3000/services.html", "services")
        finally:
            context.close()
            browser.close()
