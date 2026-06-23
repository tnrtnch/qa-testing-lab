from scrapy.http import HtmlResponse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "kaldata_spider"

sys.path.insert(0, str(PROJECT))

from kaldata.spiders.kaldata_spider import KaldataSpiderSpider

def test_content_parser():
    html = """
    <html>
        <body>

            <h1>Test Article Title</h1>

            <time datetime="2026-06-23"></time>

            <a class="tdb-author-name">Tom Franklin</a>

            <div class="td-post-content tagdiv-type">
                <p>First paragraph.</p>
                <p>Second paragraph.</p>
            </div>

        </body>
    </html>
    """

    response = HtmlResponse(
        url="https://example.com/article",
        body=html,
        encoding="utf-8"
    )

    spider = KaldataSpiderSpider()

    results = list(spider.content(response))

    assert len(results) == 1

    item = results[0]

    assert item["title"] == "Test Article Title"
    assert item["pubdate"] == "2026-06-23"
    assert item["author"] == "Tom Franklin"

    assert "First paragraph." in item["body"]
    assert "Second paragraph." in item["body"]