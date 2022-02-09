from Domain.obiect import creeaza_obiect, get_id


def adauga_obiect(id, nume, descriere, pret, locatie, lista):
    """
    Adauga un obiect in lista
    :param id: id-ul obiectului
    :param nume: numele obiectului
    :param descriere: descrierea obiectului
    :param pret: pretul obiectului
    :param locatie: locatia obiectului
    :param lista: lista de obiecte
    :return: o lista care contine lista veche si noul obiect
    """
    if get_by_id(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    obiect = creeaza_obiect(id, nume, descriere, pret, locatie)
    return lista + [obiect]


def get_by_id(id, lista):
    """
    indica obiectul cu id-ul dat dintr-o lista
    :param id: id-ul dat
    :param lista: o lista de obiecte
    :return: obiectul cu id-ul dat din lista sau None, daca aceasta nu exista
    """
    for obiect in lista:
        if get_id(obiect) == id:
            return obiect
    return None


def sterge_obiect(id, lista):
    """
    Sterge un obiect dintr-o lista dupa id
    :param id: id-ul obiectului ce trebuie sters
    :param lista:lista de obiecte din inventar
    :return: lista dupa ce a fost facuta modificarea
    """
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista un inventar cu id-ul dat!")
    return [obiect for obiect in lista if get_id(obiect) != id]


def modifica_obiect(id, nume, descriere, pret, locatie, lista):
    """
    Modifica obiectul din lista cu id-ul dat
    :param id: id-ul obiectului
    :param nume: numele obiectului
    :param descriere: descrierea obiectului
    :param pret: pretul obiectului
    :param locatie: locatia obiectului
    :param lista: lista de obiecte
    :return: lista modificata
    """
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista un obiect cu id-ul dat!")
    lista_noua = []
    for obiect in lista:
        if get_id(obiect) == id:
            obiect_nou = creeaza_obiect(id, nume, descriere, pret, locatie)
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua
