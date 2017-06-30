"""Tests against the generated json file."""
from helpers import _load_site


def test_duplicate_permalinks():
    """Test to see that no entries point to the same url."""
    site = _load_site()
    links = {}
    for entry in site:
        url = site[entry]['url']
        if url in links.keys():
            assert entry == links[url]
        else:
            links[url] = entry
