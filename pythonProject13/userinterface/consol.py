from domain.obiect import get_str
from logic.crud import adauga_obiect, stergere_obiect, modificare_obiect
from logic.probleme import concatenare, lista_locatii_obiecte, pret_maxim_locatii, ordonare_obiecte, mutare_locatie, \
    suma_pret_locatie
from userinterface.command_line_console import command_line_console


def print_menu():
    print("1. Adaugarea unui obiect")
    print("2. Stergerea unui obiect")
    print("3. Modificarea unui obiect")
    print("4. Mutarea tuturor obiectelor dintr-o locație în alta.")
    print("5. Concatenarea unui string citit la toate descrierile cu proprietatea ceruta")
    print("6. Determinarea pretului maxim pentru fiecare locație.")
    print("7. Ordonarea obiectelor crescător după preț.")
    print("8. Afișarea sumelor prețurilor pentru fiecare locație.")
    print("9. Undo")
    print("10. consol")
    print("a. Afisare toate obiectele")
    print("x. Iesire")


def ui_adaugare_obiect(lista):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        descriere = input("Dati descrierea: ")
        pret = float(input("Dati pretul: "))
        locatie = input("Dati locatia: ")
        return adauga_obiect(lista, id, nume, descriere, pret, locatie)
    except ValueError as ve:
        print("eroare: {}".format(ve))
        return lista


def ui_stergere_obiect(lista):
    try:
        id = input("Dati id-ul obiectului  pe care doriti sa il stergeti: ")
        return stergere_obiect(id, lista)
    except ValueError as ve:
        print("eroare:  {}".format(ve))
        return lista


def ui_modificare_obiect(lista):
    try:
        id = input("Dati id-ul obiectului pe care doriti sa il modificati: ")
        nume = input("Dati numele: ")
        descriere = input("Dati descrierea: ")
        pret = input("Dati pretul: ")
        locatie = input("Dati locatia: ")
        return modificare_obiect(lista, id, nume, descriere, pret, locatie)
    except ValueError as ve:
        print("eroare: {}".format(ve))
        return lista


def ui_concatenare(lista):
    try:
        string_citit = input("Dati string-ul: ")
        if string_citit == "":
            raise ValueError("String-ul este nenul")
        pret_citit = float(input("Dati pretul: "))
        return concatenare(lista, pret_citit, string_citit)
    except ValueError as ve:
        print("eroare", ve)
        return lista


def ui_pret_maxim_locatii(lista):
    lista_locatie = lista_locatii_obiecte(lista)
    lista_pret = pret_maxim_locatii(lista)
    for x in range(0, len(lista_pret)):
        print(lista_locatie[x], ": ", lista_pret[x])


def ui_ordonare_obiecte(lista):
    afisare(ordonare_obiecte(lista))


def ui_mutare(lista):
    try:
        locatie1 = input("Dati locatia din care sa se mute obiectele: ")
        locatie2 = input("Dati noua locatie: ")
        if locatie2 == "" or locatie1 == "":
            raise ValueError("Locatia este nenula")
        return mutare_locatie(lista, locatie1, locatie2)
    except ValueError as ve:
        print("eroare", ve)
        return lista


def afisare(lista):
    for obiect in lista:
        print(get_str(obiect))


def ui_suma_pret_locatie(lista):
    lista1 = lista_locatii_obiecte(lista)
    lista2 = suma_pret_locatie(lista)
    for x in range(0, len(lista2)):
        print(lista1[x], ": ", lista2[x])


def ui_command_line_console(lista):
    return command_line_console(lista)


def run_menu(lista):
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = ui_adaugare_obiect(lista)
        elif optiune == "2":
            lista = ui_stergere_obiect(lista)
        elif optiune == "3":
            lista = ui_modificare_obiect(lista)
        elif optiune == "4":
            lista = ui_mutare(lista)
        elif optiune == "5":
            lista = ui_concatenare(lista)
        elif optiune == "6":
            ui_pret_maxim_locatii(lista)
        elif optiune == "7":
            ui_ordonare_obiecte(lista)
        elif optiune == "a":
            afisare(lista)
        elif optiune == "8":
            ui_suma_pret_locatie(lista)
        elif optiune == "9":
            pass
        elif optiune == "10":
             lista = ui_command_line_console(lista)
        elif optiune == "x":
            return 0
        else:
            print("Dati alta optiune")
