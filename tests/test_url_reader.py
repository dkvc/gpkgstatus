from pytest import raises

from gpkgstatus.URLReader import URLReader

"""
These tests require an working internet connection.
"""
class TestURLReader():
    def test_site_that_exists(self):
        assert isinstance(URLReader("https://www.python.org"), URLReader)
    
    def test_site_404_not_found(self):
        with raises(Exception):
            URLReader("https://httpstat.us/404")

    def test_site_does_not_exist(self):
        with raises(SystemExit):
            URLReader("https://websitenotexists.py/")