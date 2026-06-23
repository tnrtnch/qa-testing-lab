from playwright.sync_api import sync_playwright

def test_sanity_table_loads():
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

        # link
        link = relps.locator("text=Ver total de proveedores sancionados")
        assert link.count() > 0

        link.first.click()

        # TABLO SANITY CHECK
        table = relps.locator("(//tbody)[5]")

        # kritik sanity assertion
        assert table.count() > 0

        # ekstra güçlü check (önerilir)
        rows = relps.locator("(//tbody)[5]//tr")
        assert rows.count() > 0

        browser.close()