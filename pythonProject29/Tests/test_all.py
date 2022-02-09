from Tests.test_crud import test_adauga_obiect, test_get_by_id, test_modifica_obiect, test_sterge_obiect
from Tests.test_domain import test_obiect
from Tests.test_functionalitati import test_modificare_locatie_obiecte, test_pret_maxim_locatie,\
      test_ordonare_crescator_dupa_pret, test_concatenare_string_citit
from Tests.test_undo_redo import test_undo_redo


def run_all_tests():
    test_obiect()
    test_adauga_obiect()
    test_modificare_locatie_obiecte()
    test_concatenare_string_citit()
    test_pret_maxim_locatie()
    test_ordonare_crescator_dupa_pret()
    test_sterge_obiect()
    test_get_by_id()
    test_modifica_obiect()
    test_undo_redo()

