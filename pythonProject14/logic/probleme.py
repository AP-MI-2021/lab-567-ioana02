from domain.obiect import get_pret, get_descriere, get_id, get_nume, get_locatie, creeaza_obiect


def concatenare(lista, pret_citit, string_citit):
    """
         concateneaza un string citit cu descrierea obiectelor care au pretul mai mare decat o valoare citita
         :param lista: lista de obiecte
         :param pret_citit: valoarea citita
         :param string_citit: string citit
         :return: o lista noua in care descriera obiectelor cu pret mai mare decat o valoare citita este concatenat cu un string citit

    """
    lista_noua = []
    for obiect in lista:
        if get_pret(obiect) > pret_citit:
            descriere_noua = get_descriere(obiect)
            descriere_noua = descriere_noua + " "
            descriere_noua = descriere_noua + string_citit
            obiect_nou = creeaza_obiect(get_id(obiect), get_nume(obiect), descriere_noua, get_pret(obiect), get_locatie(obiect))
            lista_noua.append(obiect_nou)
        else:
            lista_noua.append(obiect)
    return lista_noua


def lista_locatii_obiecte(lista):
    """
    Creeaza o lista cu locatiile obiectelor
    :param lista: lista cu obiectele
    :return: o lista cu locatiile obiectelor
    """
    lista_noua = []
    for obiect in lista:
        if get_locatie(obiect) not in lista_noua:
            lista_noua.append(get_locatie(obiect))
    return lista_noua


def pret_maxim_locatii(lista):
    """
      Adauga intr-o lista cu preturile obiectelor pretul obiectului cu locatia x si pretul maxim
      :param lista: lista obiecte
      :return: o lista noua
    """
    lista_noua = lista_locatii_obiecte(lista)
    lista_preturi = []
    for x in lista_noua:
        maxim = 0
        for obiect in lista:
            if get_locatie(obiect) == x and get_pret(obiect) > maxim:
                maxim = get_pret(obiect)
        lista_preturi.append(maxim)
    return lista_preturi


def ordonare_obiecte(lista):
    """
    Ordoneaza crescator obiectele dupa pret
    :param lista: lista de obiecte
    :return: lista cu obiectele ordonate crescator dupa pret
    """
    for i in range(0, len(lista)-1):
        for j in range(i+1, len(lista)):
            if float(get_pret(lista[i])) > float(get_pret(lista[j])):
                lista[i], lista[j] = lista[j], lista[i]
    return lista
