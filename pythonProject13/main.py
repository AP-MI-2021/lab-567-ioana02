from tests.teste import run_all_tests
from userinterface.command_line_console import command_line_console
from userinterface.consol import run_menu


def alegere_optiune():
    print("1. console")
    print("2. command line")
    print("x. exit")


def main():
    run_all_tests()
    while True:
        alegere_optiune()
        alegere = input("Dati optiunea: ")
        if alegere == "1":
            run_menu([])
        elif alegere == "2":
            command_line_console([])
        elif alegere == "x":
            break
        else:
            print("Dati alta optiune")


if __name__ == "__main__":
    main()
