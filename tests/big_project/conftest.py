import pytest

from sub_project.module0 import Module0
# noinspection PyUnresolvedReferences
from sub_project_test_support.fixtures import sub0_module1_fixture


@pytest.fixture
def fixture0() -> Module0:
    print('fixture0')
    return Module0()