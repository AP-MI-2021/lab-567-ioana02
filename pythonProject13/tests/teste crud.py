from domain.obiect import creeaza_obiect, get_id, get_nume, get_descriere, get_pret, get_locatie
from logic.crud import adauga_obiect, read, modificare_obiect, stergere_obiect


def test_adauga_obiect():
    id = 2
    nume = "masa"
    descriere = "culoare maro"
    pret = 35
    locatie = "asmn"
    lista = []
    obiect = creeaza_obiect(id, nume, descriere, pret, locatie)
    adauga_obiect(lista, id, nume, descriere, pret, locatie)
    assert lista == [obiect]
    assert len(lista) == 1
    assert get_id(read(lista, 2)) == 2
    assert get_nume(read(lista, 2)) == "masa"
    assert get_descriere(read(lista, 2)) == "culoare maro"
    assert get_pret(read(lista, 2)) == 35
    assert get_locatie(read(lista, 2)) == "asmn"


def test_read():
    lista = []
    id = 1
    nume = "minge"
    descriere = "rosie"
    pret = 24
    locatie = "asbn"
    obiect = creeaza_obiect(id, nume, descriere, pret, locatie)
    adauga_obiect(lista, id, nume, descriere, pret, locatie)
    id = 3
    nume = "minge"
    descriere = "verde"
    pret = 23
    locatie = "absm"
    obiect = creeaza_obiect(id, nume, descriere, pret, locatie)
    adauga_obiect(lista, id, nume, descriere, pret, locatie)
    assert get_id(read(lista, 1)) == 1
    assert get_id(read(lista, 3)) == 3


def test_stergere():
    lista = []
    id = 1
    nume = "minge"
    descriere = "rosie"
    pret = 24
    locatie = "asbn"
    obiect = creeaza_obiect(id, nume, descriere, pret, locatie)
    adauga_obiect(lista, id, nume, descriere, pret, locatie)
    id = 3
    nume = "minge"
    descriere = "verde"
    pret = 23
    locatie = "absm"
    obiect = creeaza_obiect(id, nume, descriere, pret, locatie)
    adauga_obiect(lista, id, nume, descriere, pret, locatie)
    lista = stergere_obiect(3, lista)
    assert len(lista) == 1
    assert read(lista, 3) is None
    assert read(lista, 1) is not None


def test_modificare_obiect():
    lista = []
    id = 1
    nume = "minge"
    descriere = "rosie"
    pret = 24
    locatie = "asbn"
    obiect = creeaza_obiect(id, nume, descriere, pret, locatie)
    adauga_obiect(lista, id, nume, descriere, pret, locatie)
    id = 3
    nume = "minge"
    descriere = "verde"
    pret = 23
    locatie = "absm"
    obiect = creeaza_obiect(id, nume, descriere, pret, locatie)
    adauga_obiect(lista, id, nume, descriere, pret, locatie)
    lista = modificare_obiect(lista, 3, "masa", "culoare maro", 234, "asbm")
    assert get_id(read(lista, 3)) == 3
    assert get_pret(read(lista, 3)) == 234
    assert get_nume(read(lista, 3)) == "masa"
    assert get_descriere(read(lista, 3)) == "culoare maro"
