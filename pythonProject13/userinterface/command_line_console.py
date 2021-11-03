from logic.crud import adauga_obiect, modificare_obiect, stergere_obiect


def print_menu():
    print("adaugare. Adaugare obiect")
    print("stergere. Stergere obiect")
    print("modificare. Modificare obiect")
    print("afisare. Afisare obiecte")
    print("exit")


def command_line_console(lista):
    lista = []
    while True:
        print_menu()
        optiune = []
        string_citit = input("Dati o optiune: ")
        optiune = string_citit.split(",")
        if optiune[0] == "adaugare":
            id = optiune[1]
            nume = optiune[2]
            descriere = optiune[3]
            pret = float(optiune[4])
            locatie = optiune[5]
            lista = adauga_obiect(lista, id, nume, descriere, pret, locatie)
            if optiune[6] == "afisare":
                print(lista)
        elif optiune[0] == "modificare":
            id = optiune[1]
            nume = optiune[2]
            descriere = optiune[3]
            pret = float(optiune[4])
            locatie = optiune[5]
            lista = modificare_obiect(lista, id, nume, descriere, pret, locatie)
            if optiune[6] == "afisare":
                print(lista)
        elif optiune[0] == "exit":
            return 0
        elif optiune[0] == "stergere":
            id = optiune[1]
            lista = stergere_obiect(lista, id)
        else:
            print("Introdu alta optiune")
