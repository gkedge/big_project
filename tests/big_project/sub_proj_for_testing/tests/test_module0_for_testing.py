import re

from runtime_syspath import print_syspath, init_std_syspath_filter

from module0_for_testing import Module0ForTesting

init_std_syspath_filter(re.compile(r'([Pp]ython|PyCharm|v\w*env)'))
print_syspath(sort=False)


def test_func0():
    assert Module0ForTesting().func0() == 'sub_pro_for_testing:module0_for_testing.py:Module0:func0'
