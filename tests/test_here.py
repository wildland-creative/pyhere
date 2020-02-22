from pyhere import __version__
from pyhere import here

def test_version():
    assert __version__ == "0.1.0"
    
def test_here():
    assert True