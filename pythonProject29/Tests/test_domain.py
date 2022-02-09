from Domain.obiect import creeaza_obiect, get_id, get_nume, get_descriere, get_pret, get_locatie


def test_obiect():
    obiect = creeaza_obiect("1", "telefon", "vorbire", 1500, "Cluj")

    assert get_id(obiect) == "1"
    assert get_nume(obiect) == "telefon"
    assert get_descriere(obiect) == "vorbire"
    assert get_pret(obiect) == 1500
    assert get_locatie(obiect) == "Cluj"
