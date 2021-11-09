from logic.crud import adauga_obiect


def test_undo_redo():
    lista = []
    undo_lista = []
    redo_lista = []

    #adaugam un obiect in lista
    undo_lista.append(lista)
    redo_lista.clear()
    lista = adauga_obiect(lista, 1, "masa", "culoare maro", 231, "absn")

    #adaugam inca un obiect
    undo_lista.append(lista)
    redo_lista.clear()
    lista = adauga_obiect(lista, 3, "minge", "verde", 23, "asmn")

    #adaugam inca un obiect
    undo_lista.append(lista)
    redo_lista.clear()
    lista = adauga_obiect(lista, 4, "minge", "rosie", 24, "asmn")

    #undo scoate ultimul obiect pe care l-am adaugat
    if len(undo_lista) > 0:
        redo_lista.append(lista)
        lista = undo_lista.pop()
    assert len(lista) == 2

    #undo scoate penultimul obiect pe care l-am adaugat
    if len(undo_lista) > 0:
        redo_lista.append(lista)
        lista = undo_lista.pop()
    assert len(lista) == 1
