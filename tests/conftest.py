import re

from runtime_syspath import add_srcdirs_to_syspath, print_syspath, init_std_syspath_filter

add_srcdirs_to_syspath()
init_std_syspath_filter(re.compile(r'([Pp]ython|PyCharm|v\w*env)'))
print_syspath(sort=False)

# Import sub_project_test_support_fixture0 from the sub-project's fixtures made available to this test module via
# the sub-project's 'src/sub_project_test_support' package. Ignore static checking that the import is not directly
# referenced in this module.
# pylint: disable=import-error,wrong-import-position
# noinspection PyUnresolvedReferences
from sub_project_test_support.fixtures import sub_project_test_support_fixture0  # noqa
# pylint: enable=import-error,wrong-import-position
