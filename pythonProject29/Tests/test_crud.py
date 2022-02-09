from Domain.obiect import get_id, get_nume, get_descriere, get_pret, get_locatie
from Logic.crud import adauga_obiect, sterge_obiect, get_by_id, modifica_obiect


def test_adauga_obiect():
    lista = adauga_obiect("1", "telefon", "vorbire", 1500, "Cluj", [])

    assert len(lista) == 1
    assert get_id(lista[0]) == "1"
    assert get_nume(lista[0]) == "telefon"
    assert get_descriere(lista[0]) == "vorbire"
    assert get_pret(lista[0]) == 1500
    assert get_locatie(lista[0]) == "Cluj"


def test_sterge_obiect():
    lista = []
    lista = adauga_obiect("1", "telefon", "vorbire", 1500, "Cluj", lista)
    lista = adauga_obiect("2", "tableta", "vorbire", 1500, "Cluj", lista)

    lista = sterge_obiect("1", lista)
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is not None


def test_get_by_id():
    lista = []
    lista = adauga_obiect("1", "telefon", "vorbire", 1500, "2348", lista)
    lista = adauga_obiect("2", "tableta", "vorbire", 1500, "Cluj", lista)
    assert get_by_id("2", lista) is not None
    assert get_by_id("5", lista) is None


def test_modifica_obiect():
    lista = []
    lista = adauga_obiect("1", "telefon", "vorbire", 1500, "2348", lista)
    lista = adauga_obiect("2", "telefon", "vorbire", 1500, "7564", lista)
    lista = modifica_obiect("1", "iphone", "vorbire", 1500, "cluj", lista)
    obiect_modificat = get_by_id("1", lista)
    assert get_nume(obiect_modificat) == "iphone"
