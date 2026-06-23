from playwright.sync_api import sync_playwright

def test_relps_iframe_exists():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto(
            "https://www3.inegi.org.mx/sistemas/ci/relps/",
            wait_until="load"
        )

        iframe_found = any(
            "relps" in frame.url.lower()
            for frame in page.frames
        )

        assert iframe_found

        browser.close()