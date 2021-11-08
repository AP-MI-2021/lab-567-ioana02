from domain.obiect import creeaza_obiect, get_id


def adauga_obiect(lst_obiecte, id, nume, descriere, pret, locatie):
    """
     Adauga un obiect nou intr-o lista
    :param lst_obiecte: lista de obiecte
    :param id: id-ul
    :param nume: numele
    :param descriere: descrierea
    :param pret: pretul
    :param locatie: locatia
    :return: o lista noua formata din lst_obiecte si noul obiect
    """
    if id < 1:
        raise ValueError("id-ul nu poate fi nul sau negativ")
    if len(nume) == 0:
        raise ValueError("numele nu poate sa fie nul")
    if len(descriere) == 0:
        raise ValueError("descrierea nu poate sa fie nula")
    if pret < 1:
        raise ValueError("pretul nu poate sa fie negativ sau nul")
    if len(locatie) != 4:
        raise ValueError("locatie trebuie sa fie formata din exact 4 caractere")
    obiect = creeaza_obiect(id, nume, descriere, pret, locatie)
    return lst_obiecte + [obiect]


def modificare_obiect(lst_obiecte, id, nume, descriere, pret, locatie):
    """
    Actualizeaza un obiect
    :param lst_obiecte: lista de obiecte
    :param id: id-ul
    :param nume: numele
    :param descriere: descrierea
    :param pret: pretul
    :param locatie: locatia
    :return: o lista cu obiectele actualizate
    """
    if read(lst_obiecte, id) is None:
        raise ValueError("obiectul cu id-ul introdus nu exista")
    if id < 1:
        raise ValueError("id-ul nu poate fi nul sau negativ")
    if len(nume) == 0:
        raise ValueError("numele nu poate sa fie nul")
    if len(descriere) == 0:
        raise ValueError("descrierea nu poate sa fie nula")
    if pret < 1:
        raise ValueError("pretul nu poate sa fie negativ sau nul")
    if len(locatie) != 4:
        raise ValueError("locatie trebuie sa fie formata din exact 4 caractere")
    noua_lst = []
    for obiect in lst_obiecte:
        if get_id(obiect) == id:
            obiect_nou = creeaza_obiect(id, nume, descriere, pret, locatie)
            noua_lst.append(obiect_nou)
        else:
            noua_lst.append(obiect)
    return noua_lst


def stergere_obiect(lst_obiecte, id):
    """
    Sterge un obiect din lista
    :param lst_obiecte: lista de obiecte
    :param id: id-ul
    :return: o lista noua fara obiectul cu id-ul id
    """
    if read(lst_obiecte, id) is None:
        raise ValueError("obiectul cu id-ul introdus nu exista")
    noua_lst = []
    for obiect in lst_obiecte:
        if get_id(obiect) != id:
            noua_lst.append(obiect)
    return noua_lst


def read(lst_obiecte, id: int):
    """
    ia obiectul cu id-ul id dintr-o lista
    :param lst_obiecte: o lista de obiecte
    :param id: id-ul
    :return: obiectul cu id-ul id sau lista cu toate obiectele, daca id=None
    """
    for obiect in lst_obiecte:
        if get_id(obiect) == id:
            return obiect
    return None
