from domain.obiect import get_str
from logic.crud import adauga_obiect, stergere_obiect, modificare_obiect
from logic.probleme import concatenare, lista_locatii_obiecte, pret_maxim_locatii, ordonare_obiecte


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
    print("a. Afisare toate obiectele")
    print("x. Iesire")


def ui_adaugare_obiect(lista):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    descriere = input("Dati descrierea: ")
    pret = float(input("Dati pretul: "))
    locatie = input("Dati locatia: ")
    return adauga_obiect(lista, id, nume, descriere, pret, locatie)


def ui_stergere_obiect(lista):
    id = input("Dati id-ul obiectului  pe care doriti sa il stergeti: ")
    return stergere_obiect(id, lista)


def ui_modificare_obiect(lista):
    id = input("Dati id-ul obiectului pe care doriti sa il modificati: ")
    nume = input("Dati numele: ")
    descriere = input("Dati descrierea: ")
    pret = input("Dati pretul: ")
    locatie = input("Dati locatia: ")
    return modificare_obiect(lista, id, nume, descriere, pret, locatie)


def ui_concatenare(lista):
    string_citit = input("Dati string-ul: ")
    pret_citit = float(input("Dati pretul: "))
    return concatenare(lista, pret_citit, string_citit)


def ui_pret_maxim_locatii(lista):
    lista_locatie = lista_locatii_obiecte(lista)
    lista_pret = pret_maxim_locatii(lista)
    for x in range(0, len(lista_pret)):
        print(lista_locatie[x], ": ", lista_pret[x])


def ui_ordonare_obiecte(lista):
    afisare(ordonare_obiecte(lista))


def afisare(lista):
    for obiect in lista:
        print(get_str(obiect))


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
            pass
        elif optiune == "5":
            lista = ui_concatenare(lista)
        elif optiune == "6":
            ui_pret_maxim_locatii(lista)
        elif optiune == "7":
            ui_ordonare_obiecte(lista)
        elif optiune == "a":
            afisare(lista)
        elif optiune == "8":
            pass
        elif optiune == "9":
            pass
        elif optiune == "x":
            return 0
        else:
            print("Dati alta optiune")
