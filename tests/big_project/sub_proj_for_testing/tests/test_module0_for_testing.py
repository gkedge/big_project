from runtime_syspath import print_sorted_syspath

from module0_for_testing import Module0ForTesting

print_sorted_syspath()


def test_func0():
    assert Module0ForTesting().func0() == 'sub_pro_for_testing:module0_for_testing.py:Module0:func0'
