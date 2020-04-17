from sub_project import Module0


def test_func0(sub_project_fixture0: Module0):
    assert sub_project_fixture0.func0() == 'sub_project:module0.py:Module0:func0'
