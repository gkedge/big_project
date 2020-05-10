## [The Package]

Still, not the recommended file structure for a project, just a package example where the `big_project` package is created by having a  directory named `big_project` and minimally contains an `__init__.py` file. All the source (except and `__main__`) associated with the `big_project` *project* so far has been move from the project root directory to the package directory making them all package members.

Again is nothing special with Python to statically access the imported `big_package` modules. To statically access the content of `module0.py` within the package from `test_package.py`, the import:
```
import module0
```
... need only change to prepend the package name:
```
from big_project.module0 import Module0
```

Since the `test_package.py` script is in the same directory (project root directory) as the `big_project` package directory, all imports are statically discovered by Python automatically adding the directory containing the script run (`test_package.py`) to `sys.path`.
```
sys.path(1 paths):
	/Users/greg/PycharmProjects/big_project
```
If Pycharm couldn't find the import, it would have a red underline under it.  
*Picture of red underline*

Because, it is statically accessible, Pycharm can navigate directly to a dependency with a click. It can also dependably refactor updating all usages of a change. \[demo Module0 name refactor]

> **Reason**: Python automatically puts the directory containing the execution script in the `sys.path` for you. Equally notable is that no part of the parental chain of that directory OR the current working directory is placed in the `sys.path`! That the current working directory is the same location as the script being executed is a very rare and unusual case of serendipity.

To better illustrate what is being added to `sys.path`, tests will print out the `sys.path` contents at the start of execution.  \[open `conftest.py`]

The print out is filtered to just show `sys.path` augmentation within the project; no system or site-package paths. \[run `test_module` and highlight `sys.path in output]

Developers can run pytests in two different ways:
- `python -p pytest test_script.py` OR
- `pytest test_script.py`

Their primary difference lies with the fact that calling via `python -p pytest` **will** add the current directory to `sys.path` in addition to the directory location of the `test_script.py`.


For the case of [The Package] demo with both module and test being in the same directory, there is no difference. But, I want to make sure through each demo that follows, both ways to start a `pytest` work. So, all the tests that are added for these demos will be run sequentially using both command patterns via \[test_all_the_tests_on_cli.py] \[run `test_all_the_tests_on_cli.py`]

[The Package]: #the-package

