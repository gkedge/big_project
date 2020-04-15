import pytest

from sub_project.module1 import Module1


@pytest.fixture
def sub0_module1_fixture():
    print('sub0_module1_fixture')
    return Module1()
