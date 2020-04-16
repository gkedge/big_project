from sub_project import module1, init_func0, Module0, Module1
from sub_project_test_support import tests_utils


def test_sub_project_func_0(sub_project_fixture0: Module0, sub_project_test_support_fixture0: Module1):
    init_func0()
    tests_utils.util0()
    module1.func0()
    print(sub_project_fixture0)
    print(sub_project_test_support_fixture0)
