from Domain.obiect import to_string
from Logic.crud import adauga_obiect, sterge_obiect, modifica_obiect, get_by_id
from Logic.functionalitati import modificare_locatie_obiecte, concatenare_string_descriere, pret_maxim_locatie, \
    ordonare_crescator_dupa_pret, suma_preturi_locatie


def print_menu():
    print("1. Adaugare obiect.")
    print("2. Stergere obiect.")
    print("3. Modificare obiect.")
    print("4. Modificare locatie obiecte.")
    print(
        "5. Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.")
    print("6. Determinarea celui mai mare preț pentru fiecare locație.")
    print("7. Ordonarea obiectelor crescător după prețul de achiziție.")
    print("8. Afișarea sumelor prețurilor pentru fiecare locație.")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare toate obiectele.")
    print("x. Iesire")


def ui_adauga_obiect(lista, undo_list, redo_list, obiecte):
    try:
        if len(obiecte) == 0:
            id = input("Dati id-ul: ")
            nume = input("Dati numele: ")
            descriere = input("Dati descrierea: ")
            pret = float(input("Dati pretul: "))
            locatie = input("Dati locatia: ")
        else:
            id = obiecte[0]
            nume = obiecte[1]
            descriere = obiecte[2]
            pret = obiecte[3]
            locatie = obiecte[4]
        rezultat = adauga_obiect(id, nume, descriere, pret, locatie, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_sterge_obiect(lista, undo_list, redo_list, obiecte):
    try:
        if len(obiecte) == 0:
            id = input("Dati id-ul obiectul ce trebuie sters: ")
        else:
            id = obiecte[0]
        rezultat = sterge_obiect(id, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_modifica_obiect(lista, undo_list, redo_list, obiecte):
    try:
        if len(obiecte) == 0:
            id = input("Dati id-ul obiectului de modificat: ")
            nume = input("Dati noul nume: ")
            descriere = input("Dati noua descriere: ")
            pret = float(input("Dati noul pret: "))
            locatie = input("Dati noua locatie: ")
        else:
            id = obiecte[0]
            nume = obiecte[1]
            descriere = obiecte[2]
            pret = obiecte[3]
            locatie = obiecte[4]
        rezultat = modifica_obiect(id, nume, descriere, pret, locatie, lista)
        obiect_vechi = get_by_id(id, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def show_all(lista):
    for obiect in lista:
        print(to_string(obiect))


def ui_modificare_locatie_obiect(lista, undo_list, redo_list, obiecte):
    try:
        if len(obiecte) == 0:
            locatie_noua = input("Dati noua locatie a obiectelor: ")
        else:
            locatie_noua = obiecte[0]
        rezultat = modificare_locatie_obiecte(locatie_noua, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_concatenare_string_descriere(lista, undo_list, redo_list, obiecte):
    try:
        if len(obiecte) == 0:
            pret = float(input("Dati pretul: "))
            string = input("Dati textul ce trebuie concatenat descrierii obiectului: ")
        else:
            pret = obiecte[0]
            string = obiecte[1]
        rezultat = concatenare_string_descriere(lista, pret, string)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_pret_maxim_locatie(lista):
    preturi = pret_maxim_locatie(lista)
    for locatie in preturi:
        print("Locatia {} are pretul maxim {}".format(locatie, preturi[locatie]))


def ui_ordonare_crescator_dupa_pret(lista, undo_list, redo_list):
    rezultat = ordonare_crescator_dupa_pret(lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat


def ui_suma_preturi_locatie(lista):
    rezultat = suma_preturi_locatie(lista)
    for locatie in rezultat:
        print("Locatia {} are suma preturilor {}".format(locatie, rezultat[locatie]))


def ui_undo(lista, undo_list, redo_list):
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
    else:
        print("Nu se poate face undo!")
    return lista


def ui_redo(lista, undo_list, redo_list):
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    else:
        print("Nu se poate face redo!")
    return lista


def run_menu(lista):
    undo_list = []
    redo_list = []
    obiecte = []
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)
        elif optiune == "2":
            lista = ui_sterge_obiect(lista, undo_list, redo_list, obiecte)
        elif optiune == "3":
            lista = ui_modifica_obiect(lista, undo_list, redo_list, obiecte)
        elif optiune == '4':
            lista = ui_modificare_locatie_obiect(lista, undo_list, redo_list, obiecte)
        elif optiune == "5":
            lista = ui_concatenare_string_descriere(lista, undo_list, redo_list, obiecte)
        elif optiune == "6":
            lista = ui_pret_maxim_locatie(lista)
        elif optiune == "7":
            lista = ui_ordonare_crescator_dupa_pret(lista, undo_list, redo_list)
        elif optiune == "8":
            lista = ui_suma_preturi_locatie(lista)
        elif optiune == "u":
            lista = ui_undo(lista, undo_list, redo_list)
        elif optiune == "r":
            lista = ui_redo(lista, undo_list, redo_list)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita. Reincercati!")
