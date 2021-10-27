from domain import obiect
from domain.obiect import get_str, get_id_obiect, get_nume, get_pret, get_descriere
from logic.crud import read, delete, update, create


def show_menu():
    print("1. CRUD ")
    print("x. Exit ")


def handle_add(obiecte):
    id_obiect = int(input("Dati id-ul obiectului: "))
    nume = str(input("Dati numele obiectului: "))
    descriere = str(input("Dati descrierea obiectului: "))
    pret = float(input("Dati pretul: "))
    locatie = str(input("Dati locatia: "))
    return create(obiecte, id_obiect, nume, descriere, pret, locatie)


def handle_modify(obiecte):
    id_obiect = int(input("Dati id-ul obiectului care se modifica: "))
    nume = str(input("Dati numele obiectului: "))
    descriere = str(input("Dati descrierea obiectului: "))
    pret = float(input("Dati pretul: "))
    locatie = str(input("Dati locatia: "))
    return update(obiect, id_obiect, nume, descriere, pret, locatie)


def handle_delete(obiecte):
    id_obiect = int(input("Dati id-ul obiectului care se srterge: "))
    obiecte = delete(obiecte, id_obiect)
    print("Stergerea a fost efectuata cu succes!")
    return obiecte


def handle_show_all(obiecte):
    for ob in obiecte:
        print(get_str(ob))


def handle_show_details(obiecte):
    id_obiect = int(input("Dati id-ul obiecului pentru care doriti detalii: "))
    ob = read(obiecte, id_obiect)
    print(f'Id-ul obiectului este: {get_id_obiect(ob)}')
    print(f'Numele obiectului este: {get_nume(ob)}')
    print(f'Descrierea obiectului este: {get_descriere(ob)}')
    print(f'Pretul obiectului este: {get_pret(ob)}')


def handel_crud(obiecte):
    while True:
        print("1. Adaugare obiect")
        print("2. Modificare obiect")
        print("3. Stergere obiect")
        print("a. Afisare")
        print("d. Detalii obiect")
        print("r. Revenire")

        optiune = input("Alegeti optiunea: ")
        if optiune == '1':
            obiecte = handle_add(obiecte)
        elif optiune == '2':
            obiecte = handle_modify(obiecte)
        elif optiune == '3':
            obiecte = handle_delete(obiecte)
        elif optiune == 'a':
            handle_show_all(obiecte)
        elif optiune == 'd':
            handle_show_details(obiecte)
        elif optiune == 'r':
            break
        else:
            print("Dati alta optiune")
    return obiecte


def run_ui(obiecte):
     while True:
        show_menu()
        optiune = input("Alegeti o optiune: ")
        print()
        if optiune == '1':
            obiecte = handel_crud(obiecte)
        elif optiune == '2':
            pass
        elif optiune == '3':
            pass
        elif optiune == '4':
            pass
        elif optiune == '5':
            pass
        elif optiune == '6':
            pass
        elif optiune == 'x':
            break
        else:
            print("Dati alta optiune")
     return obiecte
