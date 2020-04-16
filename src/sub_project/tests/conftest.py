import sys
from pathlib import Path
from typing import Generator

import pytest

# TODO: Add to test_support project's package __init__.py
# PROJECT_ROOT: Path = (Path(__file__).parent / '..').resolve()
PROJECT_ROOT: Path = Path.cwd()
ALL_PROJECT_SRC_DIRS: Generator[Path, None, None] = PROJECT_ROOT.rglob('src')

for tested_src in ALL_PROJECT_SRC_DIRS:
    if tested_src.is_dir() and str(tested_src) not in sys.path:
        print(f'Adding {tested_src} to sys.path')
        sys.path.append(str(tested_src))

from sub_project import Module0

# Import sub_project_test_support_fixture0 from the sub-project's fixtures made available to this test module via
# the sub-project's 'src/sub_project_test_support' package. Ignore static checking that the import is not directly
# referenced in this module.
# noinspection PyUnresolvedReferences
from sub_project_test_support.fixtures import sub_project_test_support_fixture0


@pytest.fixture
def sub_project_fixture0() -> Module0:
    print('sub_project_fixture0')
    return Module0()
