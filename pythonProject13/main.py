from domain import obiect
from logic.crud import create
from userinterface.consol import run_ui


def main():
    obiecte = []
    obiecte = create(obiect, 12, "jucarie", "pentru copii", 26, "sasr"),
    obiecte = create(obiect, 14445, "masa", "culoare maro", 234, "sura"),
    obiecte = create(obiect, 23512, "minge", "rosie", 23, "asga"),
    run_ui(obiecte)
if_name_ == "_main"
 run_all_tests()
    main()