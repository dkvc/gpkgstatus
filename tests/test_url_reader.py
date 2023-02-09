import os

from pathlib import Path
from pytest import raises
from tempfile import gettempdir

from gpkgstatus.URLReader import URLReader


"""
These tests require an working internet connection.
"""


class TestURLReader:
    def test_site_that_exists(self):
        assert isinstance(URLReader("https://www.python.org"), URLReader)

    def test_site_404_not_found(self):
        with raises(Exception):
            URLReader("https://xkcd.com/404")

    def test_site_does_not_exist(self):
        with raises(SystemExit):
            URLReader("https://websitenotexists.py/")


class TestSavedFiles:
    def test_saved_file_exists(self):
        filename = "test_file.json"
        # python.org
        URLReader("https://2p66nmmycsj3.statuspage.io/api/v2/status.json").save_as_file(
            filename
        )

        path = Path(os.path.join(gettempdir(), filename))
        exists = path.exists()
        if exists:
            os.remove(path)
        assert exists

    def test_saved_is_file(self):
        filename = "test_file.json"
        # console status on python.org
        URLReader(
            "https://console.python.org/python-dot-org-live-consoles-status"
        ).save_as_file(filename)

        path = Path(os.path.join(gettempdir(), filename))
        is_file = path.is_file()
        if is_file:
            os.remove(path)
        assert is_file
