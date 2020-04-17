import sys
from pathlib import Path
from typing import Generator


# TODO: Add to test_support project's package __init__.py
def add_src_to_sys_path():
    all_project_src_dirs: Generator[Path, None, None] = Path.cwd().rglob('src')
    prior_sys_path = sys.path.copy()
    for tested_src in all_project_src_dirs:
        if tested_src.is_dir() and str(tested_src) not in sys.path:
            sys.path.append(str(tested_src))
    print(f'Added to sys.path: {set(prior_sys_path).symmetric_difference(set(sys.path))}')


add_src_to_sys_path()

# Import sub_project_test_support_fixture0 from the sub-project's fixtures made available to this test module via
# the sub-project's 'src/sub_project_test_support' package. Ignore static checking that the import is not directly
# referenced in this module.
# pylint: disable=import-error,wrong-import-position
# noinspection PyUnresolvedReferences
from sub_project_test_support.fixtures import sub_project_test_support_fixture0
# pylint: enable=import-error,wrong-import-position
