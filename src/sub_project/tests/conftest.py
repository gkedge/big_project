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

# noinspection PyUnresolvedReferences
from sub_project_test_support.fixtures import sub0_module1_fixture


@pytest.fixture
def sub0_module0_fixture() -> Module0:
    print('sub0_module0_fixture')
    return Module0()
