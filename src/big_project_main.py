import re

from runtime_syspath import add_srcdirs_to_syspath, print_syspath, init_std_syspath_filter

add_srcdirs_to_syspath()
init_std_syspath_filter(re.compile(r'([Pp]ython|PyCharm|v\w*env)'))
print_syspath(sort=False)

# pylint: disable=import-error,wrong-import-position
# noinspection PyUnresolvedReferences
import big_project  # noqa

# pylint: enable=import-error,wrong-import-position

print("Execute the Big Project.")


def main():
    big_prog_mod0: big_project.Module0 = big_project.Module0()
    print(big_prog_mod0.func0())


if __name__ == "__main__":
    main()
