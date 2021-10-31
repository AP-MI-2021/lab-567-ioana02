def creeaza_obiect(id: int, nume, descriere, pret, locatie: str):
    """
         Creeaza o lista care reprezinta un obiect
         :param id: id-ul obiectului, este unic
         :param nume: denumirea obiectului
         :param descriere: descrierea obiectului
         :param pret: pretul obiectului
         :param locatie: locul in care este obiectul
         :return: un  dictionar ce retine un obiect
    """
    return {
        "identi": id,
        "nume": nume,
        "descriere": descriere,
        "pret": pret,
        "locatie": locatie,
    }


def get_id(obiect):
    """
     returneaza identi-ul obiectului
    :param obiect:un dictionar de tip obiect
    :return: identi-ul obiectului
    """
    return obiect["id"]


def get_nume(obiect):
    """
    returneaza numele obiectului
    :param obiect: un dictionar de tip obiect
    :return: numele obiectului
    """
    return obiect["nume"]


def get_descriere(obiect):
    """
    returneaza descrierea obiectului
    :param obiect: un dictionar de tip obiect
    :return: descrierea obiectului
    """
    return obiect["descriere"]


def get_pret(obiect):
    """
    returneaza pretul obiectului
    :param obiect:  dictionar de tip obiect
    :return: pretul obiectului
    """
    return obiect["pret"]


def get_locatie(obiect):
    """
      returneaza locul in care este obiectul
      :param obiect:  dictionar de tip obiect
      :return: locatia obiectului
    """
    return obiect["locatie"]


def get_str(obiect):
    ob = {"id": get_id(obiect), "nume": get_nume(obiect), "descriere": get_descriere(obiect), "pret": get_pret(obiect), "locatie": get_locatie(obiect)}
    lista = list(ob.items())
    return lista


def valideaza_obiect(obiect):
    if len(get_locatie(obiect)) > 4:
        raise ValueError("Locatia are maxim 4 caractere")
