from playwright.sync_api import sync_playwright

def test_site_accessible():
    print("Starting test")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        print("Opening page")

        page.goto(
            "https://www3.inegi.org.mx/sistemas/ci/relps/",
            wait_until="load"
        )
        print("Page opened")


        assert "inegi.org.mx" in page.url

        browser.close()