def creeaza_obiect(id, nume, descriere, pret, locatie):
    """
    creeaza un dictionar ce retine un obiect
    :param id: id-ul obiectului
    :param nume: numele obiectului
    :param descriere: descrierea obiectului
    :param pret: pretul obiectului
    :param locatie: locatia obiectului
    :return:un dictionar ce retine un obiect
    """
    if id == "" or nume == "" or descriere == "":
        raise ValueError("Id-ul, numele si descrierea trebuie sa fie nenule.")
    if pret is not None and not isinstance(pret, (float, int)):
        raise ValueError("Pretul trebuie sa fie un numar.")
    if pret is None:
        raise ValueError("Pretul nu poate sa fie nul.")
    if pret < 0:
        raise ValueError("Pretul nu poate sa fie negativ.")
    if locatie is not None and len(locatie) != 4:
        raise ValueError("Locatia trebuie sa fie formata doar din 4 caractere.")
    return [id, nume, descriere, pret, locatie]

    # return {
    #   "id": id,
    #  "nume": nume,
    # "descriere": descriere,
    # "pret": pret,
    # "locatie": locatie
    # }


def get_id(obiect):
    """
    indica id-ul unui obiect
    :param obiect: o lista cu obiectele
    :return: id-ul obiectului
    """
    return obiect[0]
    # return obiect["id"]


def get_nume(obiect):
    """
    indica numele unui obiect
    :param obiect: o lista de obiecte
    :return: numele obiectului
    """
    return obiect[1]
    # return obiect["nume"]


def get_descriere(obiect):
    """
    indica descrierea unui obiect
    :param obiect: o lista de obiecte
    :return: descrierea obiectului
    """
    return obiect[2]
    # return obiect["descriere"]


def get_pret(obiect):
    """
    indica pretul unui obiect
    :param obiect: o lista de obiecte
    :return: pretul obiectului
    """
    return obiect[3]
    # return obiect["pret"]


def get_locatie(obiect):
    """
    indica locatia unui obiect
    :param obiect: o lista de obiecte
    :return: locatia obiectului
    """
    return obiect[4]
    # return obiect["locatie"]


def to_string(obiect):
    return "Id: {}, Nume: {}, Descriere: {}, Pret: {}, Locatie: {}".format(
        get_id(obiect),
        get_nume(obiect),
        get_descriere(obiect),
        get_pret(obiect),
        get_locatie(obiect)
    )
