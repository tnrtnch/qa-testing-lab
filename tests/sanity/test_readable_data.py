from playwright.sync_api import sync_playwright

def test_sanity_table_has_readable_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(
            "https://www3.inegi.org.mx/sistemas/ci/relps/",
            wait_until="load"
        )

        # iframe bul
        relps = next(
            f for f in page.frames
            if "relps" in f.url.lower()
        )

        # linke git
        link = relps.locator("text=Ver total de proveedores sancionados")
        assert link.count() > 0

        link.first.click()

        # tabloyu bekle
        relps.wait_for_selector("(//tbody)[5]//tr")

        # satırlar
        rows = relps.locator("(//tbody)[5]//tr")

        assert rows.count() > 0

        # 🔥 ekstra sanity check: ilk satır boş mu?
        first_row_text = rows.nth(1).text_content()

        assert first_row_text is not None
        assert len(first_row_text.strip()) > 0

        browser.close()