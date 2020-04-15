from sub_project import module1, init_func0
from sub_project.module0 import Module0
from sub_project.module1 import Module1
from sub_project_test_support import tests_utils


def test_func_0(sub0_module0_fixture: Module0, sub0_module1_fixture: Module1):
    init_func0()
    tests_utils.util0()
    module1.sub0_mod1_func0()
    print(sub0_module0_fixture)
    print(sub0_module1_fixture)
