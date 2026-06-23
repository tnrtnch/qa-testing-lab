import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "telegraph_beautifulsoup"

sys.path.insert(0, str(PROJECT))

from scraper import fetch_articles

def test_fetch_articles_integration():
    """
    Integration test:
    requests + BeautifulSoup + parsing chain
    """

    results = list(fetch_articles())

    # -------------------------
    # BASIC VALIDATION
    # -------------------------
    assert isinstance(results, list)
    assert len(results) > 0, "No articles scraped"

    # -------------------------
    # STRUCTURE VALIDATION
    # -------------------------
    first = results[0]

    assert "title" in first
    assert isinstance(first["title"], str)
    assert first["title"].strip() != ""

    assert "body" in first
    assert isinstance(first["body"], str)

    assert "author" in first
    assert isinstance(first["author"], str)

    assert "url" in first
    assert first["url"].startswith("http")

    assert "scraped_at" in first

    # -------------------------
    # CONTENT VALIDATION
    # -------------------------
    assert len(first["body"]) > 20, "Body too short (parse issue?)"