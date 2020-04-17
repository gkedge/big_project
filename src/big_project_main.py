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

# pylint: disable=import-error,wrong-import-position
import big_project
from big_project import Module0

# pylint: enable=import-error,wrong-import-position\

print("Execute the Big Project.")


def main():
    big_prog_mod0: Module0 = big_project.Module0()
    print(big_prog_mod0.func0())


if __name__ == "__main__":
    main()
