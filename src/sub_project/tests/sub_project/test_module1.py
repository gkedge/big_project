from sub_project.module1 import Module1


def test_func0():
    assert Module1().func0() == 'sub_project:module1.py:Module1:func0'
