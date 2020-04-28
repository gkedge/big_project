from sub_project.module0 import Module0


def test_sub_project_fixture0(sub_project_fixture0: Module0):
    assert isinstance(sub_project_fixture0, Module0)
