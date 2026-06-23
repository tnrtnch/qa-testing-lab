from playwright.sync_api import sync_playwright

def test_selector_regression():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(
            "https://www3.inegi.org.mx/sistemas/ci/relps/",
            wait_until="load"
        )

        relps = next(
            f for f in page.frames
            if "relps" in f.url.lower()
        )

        link = relps.locator("text=Ver total de proveedores sancionados")
        link.first.click()

        relps.wait_for_selector("(//tbody)[5]")

        #SELECTOR KONTROLÜ
        selector = relps.locator("//tr[@align='center']//td[@align='left']")

        assert selector.count() > 0

        browser.close()