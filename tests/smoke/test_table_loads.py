from playwright.sync_api import sync_playwright

def test_table_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto(
            "https://www3.inegi.org.mx/sistemas/ci/relps/",
            wait_until="load"
        )

        page.wait_for_timeout(2000)

        relps = next(
            f for f in page.frames
            if "relps" in f.url.lower()
        )

        relps.locator(
            "text=Ver total de proveedores sancionados"
        ).click()

        relps.wait_for_selector("(//tbody)[5]")

        rows = relps.locator("(//tbody)[5]//tr")

        assert rows.count() > 0

        browser.close()