from logic.crud import adauga_obiect


def test_undo_redo():
    lista = []
    undo_lista = []
    redo_lista = []

    #adaugam un obiect in lista
    undo_lista.append(lista)
    redo_lista.clear()
    lista = adauga_obiect(lista, 1, "masa", "culoare maro", 231, "absn")

    #adaugam inca un obiect in lista
    undo_lista.append(lista)
    redo_lista.clear()
    lista = adauga_obiect(lista, 3, "minge", "verde", 23, "asmn")

    #adaugam inca un obiect in lista
    undo_lista.append(lista)
    redo_lista.clear()
    lista = adauga_obiect(lista, 4, "minge", "rosie", 24, "asmn")

    #undo scoate ultimul obiect pe care l-am adaugat in lista
    if len(undo_lista) > 0:
        redo_lista.append(lista)
        lista = undo_lista.pop()
    assert len(lista) == 2

    #undo scoate penultimul obiect pe care l-am adaugat in lista
    if len(undo_lista) > 0:
        redo_lista.append(lista)
        lista = undo_lista.pop()
    assert len(lista) == 1

    #inca un undo nu face nimic
    if len(undo_lista) > 0:
        redo_lista.append(lista)
        lista = undo_lista.pop()
    assert len(lista) == 0

    #adaugam inca trei obiecte in lista
    undo_lista.append(lista)
    redo_lista.clear()
    lista = adauga_obiect(lista, 5, "masa", "culoare maro", 231, "absn")
    undo_lista.append(lista)
    redo_lista.clear()
    lista = adauga_obiect(lista, 6, "jucarie", "copii", 22, "absm")
    undo_lista.append(lista)
    redo_lista.clear()
    lista = adauga_obiect(lista, 7, "minge", "rosie", 231, "absn")

    #redo nu face nimic
    if len(redo_lista) > 0:
        undo_lista.append(lista)
        lista = redo_lista.pop()
    assert len(lista) == 3

    # doua undo-uri scot ultimele 2 obiecte
    if len(undo_lista) > 0:
        redo_lista.append(lista)
        lista = undo_lista.pop()
    if len(undo_lista) > 0:
        redo_lista.append(lista)
        lista = undo_lista.pop()
    assert len(lista) == 1

    # redo anuleaza ultimul undo, daca ultima operatie e undo
    if len(redo_lista) > 0:
        undo_lista.append(lista)
        lista = redo_lista.pop()
    assert len(lista) == 2

    # redo anuleaza si primul undo
    if len(redo_lista) > 0:
        undo_lista.append(lista)
        lista = redo_lista.pop()
    assert len(lista) == 3

    # doua undo-uri scot ultimele 2 obiecte
    if len(undo_lista) > 0:
        redo_lista.append(lista)
        lista = undo_lista.pop()
    if len(undo_lista) > 0:
        redo_lista.append(lista)
        lista = undo_lista.pop()
    assert len(lista) == 1

    # adaugam un obiect
    undo_lista.append(lista)
    redo_lista.clear()
    lista = adauga_obiect(lista, 23, "masa", "culoare maro", 355, "asbn")

    # redo nu face nimic, deoarece ultima operatie nu este un undo
    if len(redo_lista) > 0:
        undo_lista.append(lista)
        lista = redo_lista.pop()
    assert len(lista) == 2

    # undo anuleaza adaugarea lui o4
    if len(undo_lista) > 0:
        redo_lista.append(lista)
        lista = undo_lista.pop()
    assert len(lista) == 1

    # undo anuleaza adaugarea lui o1 - practic se continua sirul de undo de la pct 14
    if len(undo_lista) > 0:
        redo_lista.append(lista)
        lista = undo_lista.pop()
    assert len(lista) == 0

    # se anuleaza ultimele 2 undo-uri
    if len(redo_lista) > 0:
        undo_lista.append(lista)
        lista = redo_lista.pop()
    if len(redo_lista) > 0:
        undo_lista.append(lista)
        lista = redo_lista.pop()
    assert len(lista) == 2

    # redo nu face nimic
    if len(redo_lista) > 0:
        undo_lista.append(lista)
        lista = redo_lista.pop()
    assert len(lista) == 2
