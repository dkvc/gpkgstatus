from gpkgstatus.JSONFileReader import JSONFileReader
from pytest import raises

class TestJSONFileReader():
    def test_less_keys(self):
        with raises(SystemExit):
            JSONFileReader("test.py")
    
    def test_invalid_file(self):
        with raises(SystemExit):
            keys = ["test", "dev", "beta"]
            JSONFileReader("test.py", *keys)