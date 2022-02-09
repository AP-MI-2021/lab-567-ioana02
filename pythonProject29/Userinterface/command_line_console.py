from Domain.obiect import to_string
from Logic.crud import adauga_obiect, sterge_obiect


def show_all(lista):
    for obiect in lista:
        print(to_string(obiect))


def main_line(lista):
    print("scrieti ajutor (pt a vedea comenzile disponibile) sau dati comanda: ")
    while True:
        given_string = input()
        if given_string == "ajutor":
            print("add, id, nume, descriere, pret, locatie")
            print("delete,id")
            print("showall")
            print("exit")
        else:
            optiuni = given_string.split(";")
            if optiuni[0] == "exit":
                break
            else:
                for optiune in optiuni:
                    opt = optiune.split(",")
                    if (opt[0] == "add"):
                        try:
                            lista = adauga_obiect(opt[1], opt[2], opt[3], float(opt[4]), opt[5], lista)
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                    elif opt[0] == "showall":
                        show_all(lista)
                    elif opt[0] == "delete":
                        lista = sterge_obiect(opt[1], lista)
                    else:
                        print("Optiune gresita! Scrieti 'ajutor' pentru a vedea optiunile disponibile.")
