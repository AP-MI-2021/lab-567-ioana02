def creeaza_obiect(id_obiect: int, nume, descriere, pret, locatie: str ):
    """
         Creeaza un dictionar care reprezinta un obiect
         :param id_obiect: id-ul obiectului, este unic
         :param nume: denumirea obiectului
         :param descriere: descrierea obiectului
         :param pret: pretul obiectului
         :param locatie: locul in care este obiectul
         :return: un obiect
    """
    return {
        "id_obiect": id-ul,
        "nume": numele,
        "descriere": descrierea,
        "pret": pretul,
        "locatie": locul,
    }
    #return [id_obiect, nume, descriere, pret, locatie]


def get_id_obiect(obiect):
    """
     ia id-ul obiectului
    :param obiect: obiectul
    :return: id-ul
    """
    return obiect["id_obiect"]
#return obiect[0]

def get_nume(obiect):
    """
    ia numele obiectului
    :param obiect: obiecul
    :return: numele
    """
    return obiect["nume"]
#return obiect[1]

def get_descriere(obiect):
    """
    ia descrierea obiectului
    :param obiect: obiectul
    :return: descrierea
    """
    return obiect["descriere"]
#return obiect[2]

def get_pret(obiect):
    """
    ia pretul obiectului
    :param obiect: obiectul
    :return: pretul
    """
    return obiect["pret"]
#return obiect[3]

def get_locatie(obiect):
    """
      ia locul in care este obiectul
      :param obiect: obiectul
      :return: locatia
    """
    return obiect["locatie"]
#return obiect[4]

def get_str(obiect):
    return f'Obiectul cu id-ul {get_id_obiect(obiect)}, cu denumirea {get_nume(obiect)}, descrierea {get_descriere(obiect)} si pretul {get_pret(obiect)} se afla in locatia {get_locatie(obiect)}. '
