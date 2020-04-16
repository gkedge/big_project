from sub_project import utils


def test_func0():
    assert utils.func0() == 'sub_project:utils.py:func0'


def test_func1():
    assert utils.func1() == 'sub_project:utils.py:func1'
