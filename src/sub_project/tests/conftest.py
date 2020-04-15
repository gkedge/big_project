import pytest

from big_project.module0 import Module0
# noinspection PyUnresolvedReferences
from sub_project_test_support.fixtures import sub0_module1_fixture


@pytest.fixture
def sub0_module0_fixture() -> Module0:
    print('sub0_module0_fixture')
    return Module0()
