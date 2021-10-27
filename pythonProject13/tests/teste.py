from domain import obiect
from domain.obiect import creeaza_obiect, get_id_obiect, get_nume, get_descriere, get_pret, get_locatie
from logic.crud import read, delete, update, create


def get_date():
    return [
        creeaza_obiect(12, "jucarie", "pentru copii", 26, "sasr"),
        creeaza_obiect(14445, "masa", "culoare maro", 234, "sura"),
        creeaza_obiect(23512, "minge", "rosie", 23, "asga"),
    ]


def test_create():
    obiecte = get_date()
    params = (2423, "minge", "verde", 24, "dsfa")
    c_nou = creeaza_obiect(*params)
    noi_obiecte = create(obiecte, *params)

    assert c_nou in noi_obiecte
    assert len(noi_obiecte) == len(obiecte) + 1
    assert get_id_obiect(read(obiecte, 12)) == 12
    assert get_nume(read(obiecte, 2)) == "masa"
    assert get_descriere(read(obiecte, 2)) == "culoare maro"
    assert get_pret(read(obiecte, 3)) == 23
    assert get_locatie(read(obiecte, 1)) == "sasr"


def test_read():
    obiecte = get_date()
    some_o = obiecte[2]
    assert read(obiecte, get_id_obiect(some_o)) == some_o
    assert read(obiecte, None) == obiecte


def test_update():
    obiecte = get_date()
    o_updated = creeaza_obiect(23512, "minge", "verde", 23, "asga")
    updated = update(obiecte, 23512, "minge", "verde", 23, "asga")
    assert o_updated in updated
    assert o_updated not in obiecte
    assert len(obiecte) == len(updated)


def test_delete():
    obiecte = get_date()
    to_delete = 1
    o_deleted = read(obiect, to_delete)
    deleted = delete(obiect, to_delete)
    assert o_deleted not in deleted
    assert o_deleted in obiecte
    assert len(deleted) == len(obiecte) - 1
