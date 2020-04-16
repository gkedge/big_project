import pytest

from sub_project.module1 import Module1


@pytest.fixture
def sub_project_test_support_fixture0() -> Module1:
    return Module1()
