from Domain.obiect import get_nume, get_pret, get_locatie, get_descriere, get_id
from Logic.crud import get_by_id
from Userinterface.console import ui_adauga_obiect, ui_undo, ui_redo, ui_sterge_obiect, ui_modifica_obiect, \
    ui_modificare_locatie_obiect, ui_concatenare_string_descriere, ui_ordonare_crescator_dupa_pret


def test_undo_redo():
    # 1 lista initiala goala
    lista = []
    undo_list = []
    redo_list = []

    # 2 adaugam un obiect
    obiecte = [1, "minge", "verde", 23.0, "asmn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)

    # 3 adaugam inca un obiect
    obiecte = [2, "masa", "culoare maro", 300.0, "asbn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)

    # 4 adaugam inca un obiect
    obiecte = [3, "telefon", "comunicare", 4500.0, "acmn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)

    assert len(lista) == 3

    # 5 undo scoate ultimul obiect adaugat
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id(2, lista) is not None
    assert get_by_id(3, lista) is None

    # 6 inca un undo scoate penultimul obiect
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is None

    # 7 inca un undo scoate si primul obiect adaugat
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 0
    assert get_by_id(1, lista) is None
    assert get_by_id(2, lista) is None

    # 8 inca un undo nu va face nimic
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 0
    assert get_by_id(1, lista) is None
    assert get_by_id(2, lista) is None

    # 9 adaugam trei obiecte
    obiecte = [1, "telefon", "comunicare", 3500.0, "asmn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)
    obiecte = [2, "ceas", "ora", 900.0, "asbn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)
    obiecte = [3, "calculator", "work", 9500.0, "acmn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)

    assert len(lista) == 3

    # 10 redo nu face nimic
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert get_by_id(1, lista) is not None
    assert get_by_id(3, lista) is not None

    # 11 doua undo-uri scot ultimele 2 obiecte
    lista = ui_undo(lista, undo_list, redo_list)
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is None

    # 12 redo anuleaza ultimul undo, daca ultima operatie e undo
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is not None

    # 13 redo anuleaza si primul undo
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is not None
    assert get_by_id(3, lista) is not None

    # 14 doua undo-uri scot ultimele 2 obiecte
    lista = ui_undo(lista, undo_list, redo_list)
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is None

    # 15 adaugam un obiect
    obiecte = [4, "jucarie", "copii", 150.0, "admn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)

    assert len(lista) == 2

    # 16 redo nu face nimic deoarece ultima operatie nu este undo
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id(1, lista) is not None
    assert get_by_id(4, lista) is not None

    # 17 undo anuleaza adaugarea obiectului cu id 4
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert get_by_id(1, lista) is not None
    assert get_by_id(4, lista) is None

    # 18 undo anuleaza adaugarea obiectului cu id 1
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 0
    assert get_by_id(1, lista) is None
    assert get_by_id(4, lista) is None

    # 19 se anuleaza ultimele 2 undo-uri
    lista = ui_redo(lista, undo_list, redo_list)
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is None

    # 20 redo nu face nimic
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id(4, lista) is not None
    assert get_by_id(3, lista) is None

    # 21 test undo\redo stergere obiect
    lista = []
    obiecte = [1, "minge", "verde", 23.0, "asmn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)
    obiecte = [2, "masa", "culoare maro", 300.0, "asbn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)
    obiecte = [3, "telefon", "comunicare", 4500.0, "acmn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)
    obiecte = [1]
    lista = ui_sterge_obiect(lista, undo_list, redo_list, obiecte)
    assert len(lista) == 2
    assert get_by_id(1, lista) is None
    assert get_by_id(2, lista) is not None
    assert get_by_id(3, lista) is not None
    lista = ui_undo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is not None
    assert get_by_id(3, lista) is not None
    lista = ui_redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert get_by_id(1, lista) is None
    assert get_by_id(2, lista) is not None

    # 22 test undo\redo modificare obiect
    lista = []
    obiecte = [1, "minge", "verde", 23.0, "asmn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)
    obiecte = [2, "masa", "culoare maro", 300.0, "asbn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)
    obiecte = [3, "telefon", "comunicare", 4500.0, "acmn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)
    obiecte = [1, "calculator", "jocuri", 9800.0, "admn"]
    lista = ui_modifica_obiect(lista, undo_list, redo_list, obiecte)
    assert len(lista) == 3
    assert get_nume(get_by_id(1, lista)) == "calculator"
    assert get_pret(get_by_id(1, lista)) == 9800.0
    lista = ui_undo(lista, undo_list, redo_list)
    assert get_nume(get_by_id(1, lista)) == "minge"
    assert get_pret(get_by_id(1, lista)) == 23.0
    lista = ui_redo(lista, undo_list, redo_list)
    assert get_nume(get_by_id(1, lista)) == "calculator"
    assert get_pret(get_by_id(1, lista)) == 9800.0

    # 23 test undo\redo modifcare locatie
    lista = []
    obiecte = [1, "minge", "verde", 23.0, "asmn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)
    obiecte = [2, "masa", "culoare maro", 300.0, "asbn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)
    obiecte = [3, "telefon", "comunicare", 4500.0, "acmn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)
    obiecte = ["amdn"]
    lista = ui_modificare_locatie_obiect(lista, undo_list, redo_list, obiecte)
    assert len(lista) == 3
    assert get_locatie(get_by_id(1, lista)) == "amdn"
    assert get_locatie(get_by_id(2, lista)) == "amdn"
    assert get_nume(get_by_id(1, lista)) == "minge"
    lista = ui_undo(lista, undo_list, redo_list)
    assert get_locatie(get_by_id(1, lista)) == "asmn"
    assert get_locatie(get_by_id(2, lista)) == "asbn"
    lista = ui_redo(lista, undo_list, redo_list)
    assert get_locatie(get_by_id(1, lista)) == "amdn"
    assert get_locatie(get_by_id(2, lista)) == "amdn"

    # 24 test undo\redo concatenare string
    lista = []
    obiecte = [1, "minge", "verde", 23.0, "asmn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)
    obiecte = [2, "masa", "culoare maro", 300.0, "asbn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)
    obiecte = [10.0, "noua"]
    lista = ui_concatenare_string_descriere(lista, undo_list, redo_list, obiecte)
    assert len(lista) == 2
    assert get_descriere(get_by_id(1, lista)) == "verdenoua"
    assert get_descriere(get_by_id(2, lista)) == "culoare maronoua"
    lista = ui_undo(lista, undo_list, redo_list)
    assert get_descriere(get_by_id(1, lista)) == "verde"
    assert get_descriere(get_by_id(2, lista)) == "culoare maro"
    lista = ui_redo(lista, undo_list, redo_list)
    assert get_descriere(get_by_id(1, lista)) == "verdenoua"
    assert get_descriere(get_by_id(2, lista)) == "culoare maronoua"

    # 25 test undo\redo ordonare dupa pret achizitie
    lista = []
    obiecte = [1, "minge", "verde", 23.0, "asmn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)
    obiecte = [2, "masa", "culoare maro", 300.0, "asbn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)
    obiecte = [3, "telefon", "comunicare", 4500.0, "acmn"]
    lista = ui_adauga_obiect(lista, undo_list, redo_list, obiecte)
    lista = ui_ordonare_crescator_dupa_pret(lista, undo_list, redo_list)
    assert get_id(lista[0]) == 1
    assert get_id(lista[1]) == 2
    assert get_id(lista[2]) == 3
    lista = ui_undo(lista, undo_list, redo_list)
    assert get_id(lista[0]) == 1
    assert get_id(lista[1]) == 2
    assert get_id(lista[2]) == 3
    lista = ui_redo(lista, undo_list, redo_list)
    assert get_id(lista[0]) == 1
    assert get_id(lista[1]) == 2
    assert get_id(lista[2]) == 3
