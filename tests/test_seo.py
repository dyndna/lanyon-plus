"""SEO Tests."""
from helpers import _load_site
from helpers import IGNORED_FILES

DESCRIPTION_BETWEEN_1_AND_155 = False


# Activate later
def _test_description_length():
    """Test validate that each page has a meaningful description."""
    site = _load_site()
    for entry in site:
        if entry not in IGNORED_FILES:
            if not 1 <= site[entry]['description_length'] <= 155:
                assert DESCRIPTION_BETWEEN_1_AND_155 == entry
