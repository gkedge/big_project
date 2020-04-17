from sub_project.module1 import Module1
from sub_project_test_support import tests_utils


def test_sub_project_test_support_test_utils_util0():
    assert tests_utils.util0() == 'sub_project_test_support:test_utils.py:util0'


def test_sub_project_test_support_fixture0(sub_project_test_support_fixture0: Module1):
    assert isinstance(sub_project_test_support_fixture0, Module1)
    assert sub_project_test_support_fixture0.func0() == 'sub_project:module1.py:Module1:func0'
