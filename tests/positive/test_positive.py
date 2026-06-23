from itertools import islice
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "telegraph_beautifulsoup"

sys.path.insert(0, str(PROJECT))

from scraper import fetch_articles


def test_article_has_valid_structure():
    articles = list(islice(fetch_articles(), 3))

    assert len(articles) > 0

    for article in articles:
        assert isinstance(article["title"], str)
        assert article["title"].strip() != ""

        assert isinstance(article["body"], str)
        assert len(article["body"]) > 50

        assert isinstance(article["author"], str)
        assert article["author"].strip() != ""

        assert article["url"].startswith("http")

        assert "scraped_at" in article

