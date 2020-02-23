from pyhere import __version__
from pyhere import here
from pyhere import find_root

def test_version():
    assert __version__ == "0.1.0"
    
def test_touch():
    assert True
    
def test_here():
    assert True
    
def test_set_here():
    assert True
    
def test_find_root(tmp_path):
    #r_indicator = ".here"
    
    # create /proj/r_indicator
    #f1 = tmp_path.mkdir("proj").join(r_indicator)
    
    #f2 = tmp_path.join("proj").mkdir("src").join("test")
    
    #assert find_root(str(f1)) == find_root(str(f2))

    assert True
    
    