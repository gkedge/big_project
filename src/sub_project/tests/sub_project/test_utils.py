from sub_project import utils


def test_util0():
    assert utils.util0() == 'sub_project:utils.py:util0'


def test_util1():
    assert utils.util1() == 'sub_project:utils.py:util1'
