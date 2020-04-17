import sys
from pathlib import Path
from typing import Generator

PROJECT_ROOT: Path = Path.cwd()
ALL_PROJECT_SRC_DIRS: Generator[Path, None, None] = PROJECT_ROOT.rglob('src')

for tested_src in ALL_PROJECT_SRC_DIRS:
    if tested_src.is_dir() and str(tested_src) not in sys.path:
        print(f'Adding {tested_src} to sys.path')
        sys.path.append(str(tested_src))
    else:
        print(f'NOT adding {tested_src} to sys.path')

import big_project
from big_project import Module0

print("Execute the Big Project.")

def main():
    big_prog_mod0: Module0 = big_project.Module0()
    print(big_prog_mod0.func0())


if __name__ == "__main__":
    main()
