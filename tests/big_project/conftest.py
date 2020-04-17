import pytest

from big_project.module0 import Module0


@pytest.fixture
def fixture0() -> Module0:
    return Module0()
