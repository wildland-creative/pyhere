# -*- coding: utf-8 -*-

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
    r_indicator = ".here"
    
    # create /proj/r_indicator
    f1 = tmp_path / "proj"
    f1.mkdir(parents=True, exist_ok=True)

    f2 = f1 / "src"
    f2.mkdir(parents=True, exist_ok=True)
    f2 = f2 / "test"
    
    assert find_root(f1).resolve() == find_root(f2).resolve()

    assert True
    
    