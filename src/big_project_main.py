from runtime_syspath import add_srcdirs_to_syspath, print_sorted_syspath
import big_project
from big_project import Module0

add_srcdirs_to_syspath()

print_sorted_syspath()

print("Execute the Big Project.")


def main():
    big_prog_mod0: Module0 = big_project.Module0()
    print(big_prog_mod0.func0())


if __name__ == "__main__":
    main()
