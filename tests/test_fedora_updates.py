import logging
from pytest import raises

import gpkgstatus.gpkgstatus as gpkg


class TestFedoraUpdates:
    def test_search_package_forced(self, capsys):
        search_term = ["kernel"]

        gpkg.search_pkg(
            {
                "name": search_term,
                "release": ["f"],
                "force": True,
                "limit": "5",
                "verbose": False,
                "noconfig": True,
                "moreinfo": False,
            }
        )

        captured = capsys.readouterr()
        words = (search_term[0], "Update ID", "Package Name", "Status")
        assert all(word in captured.out for word in words)

    def test_search_package(self, capsys):
        search_term = ["kernel"]

        gpkg.search_pkg(
            {
                "name": search_term,
                "release": ["f"],
                "force": False,
                "limit": "5",
                "verbose": False,
                "noconfig": True,
                "moreinfo": False,
            }
        )

        captured = capsys.readouterr()
        words = (search_term[0], "Update ID", "Package Name", "Status")
        assert all(word in captured.out for word in words)

    def test_valid_distro_forced(self, capsys):
        search_term = ["python"]

        gpkg.search_pkg(
            {
                "name": search_term,
                "release": ["f37"],
                "force": True,
                "limit": "8",
                "verbose": False,
                "noconfig": True,
                "moreinfo": False,
            }
        )

        captured = capsys.readouterr()
        words = ("f36", "f38")
        assert all(word not in captured.out for word in words)

    def test_valid_distro(self, capsys):
        search_term = ["python"]

        gpkg.search_pkg(
            {
                "name": search_term,
                "release": ["f37"],
                "force": False,
                "limit": "8",
                "verbose": False,
                "noconfig": True,
                "moreinfo": False,
            }
        )

        captured = capsys.readouterr()
        words = ("f36", "f38")
        assert all(word not in captured.out for word in words)

    def test_invalid_distro_forced(self, capsys):
        search_term = ["kernel"]

        with raises(SystemExit):
            gpkg.search_pkg(
                {
                    "name": search_term,
                    "release": "d11",
                    "force": True,
                    "limit": "2",
                    "verbose": False,
                    "noconfig": True,
                    "moreinfo": False,
                }
            )

        captured = capsys.readouterr()
        assert (
            captured.out == "Error: Invalid Distribution Release. Format: f{version}\n"
        )

    def test_invalid_distro(self, capsys):
        search_term = ["kernel"]

        with raises(SystemExit):
            gpkg.search_pkg(
                {
                    "name": search_term,
                    "release": "d11",
                    "force": False,
                    "limit": "2",
                    "verbose": False,
                    "noconfig": True,
                    "moreinfo": False,
                }
            )

        captured = capsys.readouterr()
        assert (
            captured.out == "Error: Invalid Distribution Release. Format: f{version}\n"
        )

    def search_term_does_not_exist(self, capsys):
        search_term = ["linux_in_toaster"]

        gpkg.search_pkg(
            {
                "name": search_term,
                "release": ["f"],
                "force": False,
                "limit": "8",
                "verbose": False,
                "noconfig": True,
                "moreinfo": False,
            }
        )

        captured = capsys.readouterr()
        assert captured.out == "No Updates Found. Check your arguments."

    def test_invalid_limit(self, capsys):
        search_term = ["openjdk"]

        with raises(SystemExit):
            gpkg.search_pkg(
                {
                    "name": search_term,
                    "release": ["f"],
                    "force": False,
                    "limit": "easy",
                    "verbose": False,
                    "noconfig": True,
                    "moreinfo": False,
                }
            )

        captured = capsys.readouterr()
        assert captured.out == "You must enter an integer value.\n"

    def test_limit_too_high(self, capsys):
        search_term = ["openjdk"]

        gpkg.search_pkg(
            {
                "name": search_term,
                "release": ["f"],
                "force": False,
                "limit": "8",
                "verbose": False,
                "noconfig": True,
                "moreinfo": False,
            }
        )

        captured = capsys.readouterr()
        words = (search_term[0], "Update ID", "Package Name", "Status")
        not_words = ("No Updates", "Check your arguments")
        assert all(word in captured.out for word in words) and all(
            not_word not in captured.out for not_word in not_words
        )

    def test_more_info(self, capsys):
        search_term = ["openjdk"]

        gpkg.search_pkg(
            {
                "name": search_term,
                "release": ["f"],
                "force": False,
                "limit": "8",
                "verbose": False,
                "noconfig": True,
                "moreinfo": True,
            }
        )

        captured = capsys.readouterr()

        words = (
            search_term[0],
            "Update ID",
            "Package Name",
            "Status",
            "Alias",
            "Date Submitted",
            "Severity",
            "Version Hash",
            "URL",
            "Notes",
        )
        not_words = ("No Updates", "Check your arguments")

        assert all(word in captured.out for word in words) and all(
            not_word not in captured.out for not_word in not_words
        )

    def test_verbose(self):
        search_term = ["openjdk"]

        gpkg.search_pkg(
            {
                "name": search_term,
                "release": ["f"],
                "force": False,
                "limit": "8",
                "verbose": True,
                "noconfig": True,
                "moreinfo": True,
            }
        )

        logger = logging.getLogger()
        assert logger.level == logging.INFO
