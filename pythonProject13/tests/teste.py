from tests.test_domain import test_creeaza_obiect
from tests.teste_crud import test_adauga_obiect, test_modificare_obiect, test_read, test_stergere
from tests.teste_probleme import test_concatenare, test_mutare_locatie, test_lista_locatii_obiecte, \
    test_ordonare_obiecte, test_suma_pret_locatie, test_pret_maxim_locatie


def run_all_tests():
    test_creeaza_obiect()
    test_adauga_obiect()
    test_stergere()
    test_modificare_obiect()
    test_read()
    test_concatenare()
    test_mutare_locatie()
    test_lista_locatii_obiecte()
    test_ordonare_obiecte()
    test_suma_pret_locatie()
    test_pret_maxim_locatie()
