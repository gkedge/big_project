from sub_project.module0 import Module0
from sub_project.module1 import Module1
from sub_project_test_support import tests_utils
from big_project import init_func0
from big_project import module0


def test_func_0(fixture0: Module0, sub0_module1_fixture: Module1):
    init_func0()
    tests_utils.util0()
    module0.func0()
    print(fixture0)
    print(sub0_module1_fixture)