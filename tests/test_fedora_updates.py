from pytest import raises

import gpkgstatus as gpkg

class TestFedoraUpdates():
    def test_search_package(self, capsys):
        search_term = "kernel"
        
        gpkg.main({'name': search_term, 
                   'distro_version': "f", 
                   'force': False})

        captured = capsys.readouterr()
        words = (search_term, "Update ID", "Package Name", "Status")
        assert all(word in captured.out for word in words)

    def test_valid_distro(self, capsys):
        search_term = "kernel"

        gpkg.main({'name': search_term, 
                   'distro_version': "f37", 
                   'force': False})

        captured = capsys.readouterr()
        words = ("f36", "f38")
        assert all(word not in captured.out for word in words)

    def test_invalid_distro(self):
        search_term = "kernel"

        with raises(SystemExit):
            gpkg.main({'name': search_term, 
                   'distro_version': "d11", 
                   'force': False})