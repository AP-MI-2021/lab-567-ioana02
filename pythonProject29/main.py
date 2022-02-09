from Tests.test_all import run_all_tests
from Userinterface.command_line_console import main_line
from Userinterface.console import run_menu


def main():
    run_all_tests()
    meniu = str(input("Scrieti ce fel de meniu doriti: clasic sau comenzi: "))
    if meniu == "clasic":
        run_menu([])
    elif meniu == "comenzi":
        main_line([])


if __name__ == '__main__':
    main()
