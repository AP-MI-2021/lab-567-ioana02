from domain.obiect import creeaza_obiect, get_id, get_nume, get_descriere, get_pret, get_locatie


def test_creeaza_obiect():
    obiect = creeaza_obiect(1, "minge", "rosie", 24, "asmn")
    assert get_id(obiect) == 1
    assert get_nume(obiect) == "minge"
    assert get_descriere(obiect) == "rosie"
    assert get_pret(obiect) == 24
    assert get_locatie(obiect) == "asmn"
