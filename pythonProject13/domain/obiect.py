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
    return [id, nume, descriere, pret, locatie]
    # return {
    # "id": id,
    # "nume": nume,
    # "descriere": descriere,
    # "pret": pret,
    # "locatie": locatie,
    # }


def get_id(obiect):
    """
     returneaza id-ul obiectului
    :param obiect:un dictionar de tip obiect
    :return: id-ul obiectului
    """
    # return obiect["id"]
    return obiect[0]


def get_nume(obiect):
    """
    returneaza numele obiectului
    :param obiect: un dictionar de tip obiect
    :return: numele obiectului
    """
    # return obiect["nume"]
    return obiect[1]


def get_descriere(obiect):
    """
    returneaza descrierea obiectului
    :param obiect: un dictionar de tip obiect
    :return: descrierea obiectului
    """
    # return obiect["descriere"]
    return obiect[2]


def get_pret(obiect):
    """
    returneaza pretul obiectului
    :param obiect:  dictionar de tip obiect
    :return: pretul obiectului
    """
    # return obiect["pret"]
    return obiect[3]


def get_locatie(obiect):
    """
      returneaza locul in care este obiectul
      :param obiect:  dictionar de tip obiect
      :return: locatia obiectului
    """
    # return obiect["locatie"]
    return obiect[4]


def get_str(obiect):
    ob = {"id": get_id(obiect), "nume": get_nume(obiect), "descriere": get_descriere(obiect),
          "pret": get_pret(obiect), "locatie": get_locatie(obiect)}
    lista = list(ob.items())
    return lista
