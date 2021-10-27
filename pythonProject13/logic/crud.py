from domain.obiect import creeaza_obiect, get_id_obiect


def create(lst_obiecte, id_obiect, nume, descriere, pret, locatie):
    """
     Adauga un obiect
    :param lst_obiecte: lista de obiecte
    :param id_obiect: id-ul
    :param nume: numele
    :param descriere: descrierea
    :param pret: pretul
    :param locatie: locatia
    :return: o lista noua formata din lst_obiecte si noul obiect
    """
    obiect = creeaza_obiect(id_obiect, nume, descriere, pret, locatie)
    return lst_obiecte + [obiect]


def update(lst_obiecte, id_obiect, nume, descriere, pret, locatie):
    """
    Actualizeaza un obiect
    :param lst_obiecte: lista de obiecte
    :param id_obiect: id-ul
    :param nume: numele
    :param descriere: descrierea
    :param pret: pretul
    :param locatie: locatia
    :return: o lista cu obiectele actualizate
    """
    noua_lst = []
    for obiect in lst_obiecte:
        if get_id_obiect(obiect) == id_obiect:
            obiect_nou = creeaza_obiect(id_obiect, nume, descriere, pret, locatie)
            noua_lst.append(obiect_nou)
        else:
            noua_lst.append(obiect)
    return noua_lst


def delete(lst_obiecte, id_obiect):
    """
    Sterge un obiect din lista
    :param lst_obiecte: lista de obiecte
    :param id_obiect: id-ul
    :return: o lista noua fara obiectul cu id-ul id_obiect
    """
    noua_lst = []
    for obiect in lst_obiecte:
        if get_id_obiect(obiect) != id_obiect:
            noua_lst.append(obiect)
    return noua_lst


def read(lst_obiecte, id_obiect: int = None):
    """
    Citeste un obiect din lista
    :param lst_obiecte: o lista de obiecte
    :param id_obiect: id-ul
    :return: obiectul cu id-ul id_obiect sau lista cu toate obiectele, dac id_obiect=None
    """
    obiect_id = None
    for obiect in lst_obiecte:
        if get_id_obiect(obiect) == id_obiect:
            obiect_id = obiect
    if obiect_id:
        return obiect_id
    return lst_obiecte
