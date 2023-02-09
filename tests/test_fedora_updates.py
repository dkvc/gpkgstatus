from pytest import raises

import gpkgstatus.gpkgstatus as gpkg


class TestFedoraUpdates:
    def test_search_package(self, capsys):
        search_term = "kernel"

        gpkg.main(
            {"name": search_term, "distro_version": "f", "force": False, "limit": "5"}
        )

        captured = capsys.readouterr()
        words = (search_term, "Update ID", "Package Name", "Status")
        assert all(word in captured.out for word in words)

    def test_valid_distro(self, capsys):
        search_term = "python"

        gpkg.main(
            {"name": search_term, "distro_version": "f37", "force": False, "limit": "8"}
        )

        captured = capsys.readouterr()
        words = ("f36", "f38")
        assert all(word not in captured.out for word in words)

    def test_invalid_distro(self, capsys):
        search_term = "kernel"

        with raises(SystemExit):
            gpkg.main(
                {
                    "name": search_term,
                    "distro_version": "d11",
                    "force": True,
                    "limit": "2",
                }
            )

        captured = capsys.readouterr()
        assert captured.out == "Error: Invalid Distribution. Format: f{version}\n"

    def search_term_does_not_exist(self, capsys):
        search_term = "linux_in_toaster"

        gpkg.main(
            {"name": search_term, "distro_version": "f", "force": False, "limit": "8"}
        )

        captured = capsys.readouterr()
        assert captured.out == "No Updates Found. Check your arguments."

    def test_invalid_limit(self, capsys):
        search_term = "openjdk"

        with raises(SystemExit):
            gpkg.main(
                {
                    "name": search_term,
                    "distro_version": "f",
                    "force": False,
                    "limit": "easy",
                }
            )

        captured = capsys.readouterr()
        assert captured.out == "You must enter an integer value.\n"

    def test_limit_too_high(self, capsys):
        search_term = "openjdk"

        gpkg.main(
            {"name": search_term, "distro_version": "f", "force": False, "limit": "8"}
        )

        captured = capsys.readouterr()
        words = (search_term, "Update ID", "Package Name", "Status")
        not_words = ("No Updates", "Check your arguments")
        assert all(word in captured.out for word in words) and all(
            not_word not in captured.out for not_word in not_words
        )
