from domain.obiect import creeaza_obiect, get_nume, get_descriere, get_pret, get_locatie
from logic.crud import adauga_obiect, read
from logic.probleme import concatenare, lista_locatii_obiecte, pret_maxim_locatii, ordonare_obiecte, mutare_locatie, \
    suma_pret_locatie


def test_concatenare(lista, pret_citit, string_citit):
    lista1 = []
    lista = []
    id = 1
    nume = "minge"
    descriere = "rosie"
    pret = 2434
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
    lista1 = concatenare(lista, pret_citit, string_citit)
    pret_citit = 100
    string_citit = "mare"
    assert get_nume(read(lista1, 3)) == "minge"
    assert get_descriere(read(lista1, 3)) == "verde"
    assert get_descriere(read(lista1, 1)) == "rosie mare"


def test_lista_locatii_obiecte():
    lista1 = []
    lista = []
    id = 1
    nume = "minge"
    descriere = "rosie"
    pret = 2434
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
    lista1 = lista_locatii_obiecte(lista)
    assert len(lista1) == 2
    assert lista1[0] == "asbn"
    assert lista1[1] == "absm"


def test_pret_maxim_locatie():
    lista1 = []
    lista = []
    id = 1
    nume = "minge"
    descriere = "rosie"
    pret = 2434
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
    lista1 = pret_maxim_locatii(lista)
    assert lista1[0] == 2434
    assert lista1[1] == 23


def test_ordonare_obiecte():
    lista1 = []
    lista = []
    id = 1
    nume = "minge"
    descriere = "rosie"
    pret = 2434
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
    ordonare_obiecte(lista)
    assert get_pret(lista[0]) == 23
    assert get_pret(lista[1]) == 2434


def test_mutare_locatie():
    lista1 = []
    lista = []
    id = 1
    nume = "minge"
    descriere = "rosie"
    pret = 2434
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
    lista = mutare_locatie(lista, "asbn", "asbm")
    assert len(lista) == 2
    assert get_locatie(read(lista, 1)) == "asbn"
    assert get_locatie(read(lista, 3)) == "asbm"


def test_suma_pret_locatie():
    lista1 = []
    lista = []
    id = 1
    nume = "minge"
    descriere = "rosie"
    pret = 2434
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
    lista1 = suma_pret_locatie(lista)
    assert lista1[0] == 2434
    assert lista1[1] == 23
