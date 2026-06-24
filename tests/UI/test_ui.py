from playwright.sync_api import sync_playwright


def test_relps_table_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch()

        page = browser.new_page()

        page.goto(
            "https://www3.inegi.org.mx/sistemas/ci/relps/"
        )

        iframe = None

        for frame in page.frames:
            if "relps" in frame.url.lower():
                iframe = frame
                break

        assert iframe is not None

        iframe.locator(
            "text=Ver total de proveedores sancionados"
        ).click()

        rows = iframe.locator("(//tbody)[5]//tr")

        assert rows.count() > 0

        browser.close() 