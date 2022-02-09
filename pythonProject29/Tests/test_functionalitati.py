from Domain.obiect import get_locatie, get_descriere, get_id
from Logic.crud import adauga_obiect, get_by_id
from Logic.functionalitati import modificare_locatie_obiecte, concatenare_string_descriere, pret_maxim_locatie, \
    ordonare_crescator_dupa_pret, suma_preturi_locatie


def test_modificare_locatie_obiecte():
    lista = []
    lista = adauga_obiect("4", "televizor", "vizionare", 2000.0, "2356", lista)
    lista = adauga_obiect("2", "telefon", "socializare", 5000.0, "7230", lista)
    locatieNoua = "9000"

    lista = modificare_locatie_obiecte(locatieNoua, lista)

    assert get_locatie(get_by_id("2", lista)) == "9000"
    assert get_locatie(get_by_id("4", lista)) == "9000"


def test_concatenare_string_citit():
    lista = []
    lista = adauga_obiect("4", "televizor", "vizionare", 2000.0, "2356", lista)
    lista = adauga_obiect("2", "telefon", "socializare", 5000.0, "7230", lista)
    lista = adauga_obiect("5", "tableta", "munca", 4500.0, "1567", lista)
    string = "ok"
    pret = 3000.0

    lista = concatenare_string_descriere(lista, pret, string)

    assert get_descriere(get_by_id("2", lista)) == "socializareok"
    assert get_descriere(get_by_id("4", lista)) == "vizionare"


def test_pret_maxim_locatie():
    lista = []
    lista = adauga_obiect("4", "televizor", "vizionare", 2000.0, "2356", lista)
    lista = adauga_obiect("2", "telefon", "socializare", 5000.0, "7230", lista)
    lista = adauga_obiect("5", "tableta", "munca", 4500.0, "7230", lista)
    preturi = pret_maxim_locatie(lista)
    assert len(preturi) == 2
    assert preturi["7230"] == 5000.0


def test_ordonare_crescator_dupa_pret():
    lista = []
    lista = adauga_obiect("4", "televizor", "vizionare", 2000.0, "2356", lista)
    lista = adauga_obiect("2", "telefon", "socializare", 5000.0, "7230", lista)
    lista = adauga_obiect("5", "tableta", "munca", 4500.0, "7230", lista)

    rezultat = ordonare_crescator_dupa_pret(lista)
    assert get_id(rezultat[0]) == "4"
    assert get_id(rezultat[1]) == "5"
    assert get_id(rezultat[2]) == "2"


def test_suma_preturi_locatie():
    lista = []
    lista = adauga_obiect("4", "televizor", "vizionare", 2000.0, "2356", lista)
    lista = adauga_obiect("2", "telefon", "socializare", 5000.0, "7230", lista)
    lista = adauga_obiect("5", "tableta", "munca", 4500.0, "7230", lista)

    rezultat = suma_preturi_locatie(lista)

    assert len(rezultat) == 2
    assert rezultat["7230"] == 9500.0
