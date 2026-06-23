def test_invalid_article_structure():
    article = {
        "title": "",
        "body": "",
    }

    assert article["title"] != ""