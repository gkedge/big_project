import pytest
from sub_project import Module0


@pytest.fixture
def sub_project_fixture0() -> Module0:
    print('sub_project_fixture0')
    return Module0()
