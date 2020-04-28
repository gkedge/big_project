from runtime_syspath import add_srcdirs_to_syspath, print_sorted_syspath

add_srcdirs_to_syspath()

print_sorted_syspath()

# Import sub_project_test_support_fixture0 from the sub-project's fixtures made available to this test module via
# the sub-project's 'src/sub_project_test_support' package. Ignore static checking that the import is not directly
# referenced in this module.
# pylint: disable=import-error,wrong-import-position
# noinspection PyUnresolvedReferences
from sub_project_test_support.fixtures import sub_project_test_support_fixture0  # noqa
# pylint: enable=import-error,wrong-import-position
