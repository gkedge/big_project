from big_project.module0 import Module0
from sub_project import Module1


def test_fixture0(fixture0: Module0):
    assert isinstance(fixture0, Module0)


def test_sub_project_test_support_fixture0(sub_project_test_support_fixture0: Module1):
    assert isinstance(sub_project_test_support_fixture0, Module1)
    assert sub_project_test_support_fixture0.func0() == 'sub_project:module1.py:Module0:func0'


