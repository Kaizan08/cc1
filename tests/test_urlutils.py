import pytest
from ..urlutils import urlchecker


def test_bad_url():
    urls = ['http://www.google.com', 'justinsnyder.me', 'https://www.google.com/1']
    assert urlchecker(urls) == [{'badurl': 'https://www.google.com/1', 'status_code': 404}]

def test_good_url():
    urls = ['http://www.google.com',
            'http://justinsnyder.me',
            'https://www.amazon.com/dp/product/B01E6AO69U/ref=EchoCP_dt_tile_text']
    assert urlchecker(urls) == []