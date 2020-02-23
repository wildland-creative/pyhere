# -*- coding: utf-8 -*-

import pytest

from pyhere import __version__
from pyhere import here
from pyhere import set_here
from pyhere import find_root
from pyhere import root_indicators

# this test is to ensure I don't mess up versioning
def test_version():
    assert __version__ == "0.2.0"
       
def test_here(tmp_path):
    # create dummy project
    # change working directory to src folder
    # generate here to data in data folder
    # assert paths
    assert True
    
def test_set_here(tmp_path):
    # create dummy project
    f1 = tmp_path / "proj" / "proj_dir"
    f1.mkdir(parents=True, exist_ok=True)

    # create .here in tmp_path
    set_here()
    cwd_path = tmp_path.cwd()
    assert cwd_path.joinpath(".here").exists()
    
    # create .here in /proj/proj_dir
    set_here(f1)
    assert f1.joinpath(".here").exists()
    
    # create .here in /proj/
    set_here(str(tmp_path / "proj"))
    assert tmp_path.joinpath("proj").joinpath(".here").exists()
    
@pytest.mark.parametrize(
    "r_indicator",
    root_indicators,
)
def test_find_root_from_indicator(tmp_path, r_indicator):   
    # create /proj/r_indicator
    f1 = tmp_path / "proj" / r_indicator
    f1.mkdir(parents=True, exist_ok=True)

    # create a different directory, /proj/src/test.txt
    f2 = f1 / "src" / "test.txt"
    f2.mkdir(parents=True, exist_ok=True)
    
    # verify they point to the same project root
    assert find_root(f1).resolve() == find_root(f2).resolve()

def test_find_sys_root(tmp_path):
    # create some nested directories
    f1 = tmp_path / "proj" / "another_path"

    # verify that they all recurse to the system root
    assert find_root(tmp_path).resolve() == find_root(f1).resolve()