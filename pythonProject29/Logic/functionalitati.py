from Domain.obiect import creeaza_obiect, get_id, get_nume, get_descriere, get_pret, get_locatie


def modificare_locatie_obiecte(locatie_noua, lista):
    """
    Modifica locatia obiectelor la o locatie data
    :param locatie_noua: locatia noua
    :param lista: lista de obiecte
    :return: lista modificata
    """
    if len(locatie_noua) != 4:
        raise ValueError("Locatia noua trebuie sa fie formata din 4 caractere.")
    lista_noua = []
    for obiect in lista:
        obiect_nou = creeaza_obiect(get_id(obiect), get_nume(obiect), get_descriere(obiect), get_pret(obiect),
                                    locatie_noua)
        lista_noua.append(obiect_nou)
    return lista_noua


def concatenare_string_descriere(lista, pret, string):
    """
    Concateneaza un string citit la descrierea obiectelor cu un pret mai mare decat un pret dat
    :param lista: lista de obiecte
    :param pret: pretul citit
    :param string: stringul citit
    :return: lista modificata
    """
    if pret < 0:
        raise ValueError("Pretul trebuie sa fie un numar pozitiv.")
    lista_noua = []
    for obiect in lista:
        if get_pret(obiect) > pret:
            noua_descriere = get_descriere(obiect) + string
            obiect_nou = creeaza_obiect(get_id(obiect), get_nume(obiect), noua_descriere, get_pret(obiect),
                                        get_locatie(obiect))
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua


def pret_maxim_locatie(lista):
    """
    Determina cel mai mare pret per locatie
    :param lista: lista de obiecte
    :return: pretul cel mai mare pentru fiecare locatie
    """
    preturi = {}
    for obiect in lista:
        locatie = get_locatie(obiect)
        if locatie in preturi:
            if get_pret(obiect) > preturi[locatie]:
                preturi[locatie] = get_pret(obiect)
        else:
            preturi[locatie] = get_pret(obiect)
    return preturi


def ordonare_crescator_dupa_pret(lista):
    """
    Ordoneaza obiectele crescator dupa pretul de achizitie
    :param lista: lista de obiecte
    :return: lista ordonata
    """
    return sorted(lista, key=get_pret)


def suma_preturi_locatie(lista):
    """
    Calculeaza suma preturilor pentru fiecare locatie
    :param lista: lista de obiecte
    :return: suma preturilor pentru fiecare locatie
    """
    rezultat = {}
    for obiect in lista:
        locatie = get_locatie(obiect)
        pret = get_pret(obiect)
        if locatie in rezultat:
            rezultat[locatie] = rezultat[locatie] + pret
        else:
            rezultat[locatie] = pret
    return rezultat
