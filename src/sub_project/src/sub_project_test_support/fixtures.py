import pytest

from sub_project import Module1


@pytest.fixture
def sub_project_test_support_fixture0() -> Module1:
    print('sub_project_test_support_fixture0')
    return Module1()
