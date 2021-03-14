import numpy
from KlasaProces import *

ilosc_procesow = 1000

def generator_danych(procesy):
    print("1. Wygeneruj i zapisz dane")
    print("2. Wczytaj dane")

    wybor = input("Numer opcji: ")

    if wybor == "1":
        #ilosc_procesow = int(input("Ilosc procesow: "))
        mu_przyjscia = int(input("Srednia czasow przyjscia: "))
        sigma_przyjscia = int(input("Odchylenie standardowe czasow przyjscia: "))
        mu_wykonania = int(input("Srednia czasow wykonania: "))
        sigma_wykonania = int(input("Odchylenie standardowe czasow wykonania: "))

        f = open("dane", "w")

        for i in range(ilosc_procesow):
            czas_przyjscia = abs(int(sigma_przyjscia * numpy.random.randn() + mu_przyjscia))
            czas_wykonania = abs(int(sigma_wykonania * numpy.random.randn() + mu_wykonania))

            procesy.append(Proces(czas_przyjscia, czas_wykonania, 0, 0))

            f.write(str(abs(czas_przyjscia)) + " ")
            f.write(str(abs(czas_wykonania)))
            f.write("\n")
        f.close()
    elif wybor == "2":
        nazwa_pliku = input("Podaj nazwe pliku: ")
        f_do_odczytu = open(nazwa_pliku, "r")
        f_do_zapisu = open("dane", "w")

        for linia in f_do_odczytu:
            procesy.append(Proces(int(linia.split(' ')[0]), int(linia.split(' ')[1]), 0, 0))
            f_do_zapisu.write(linia)

        f_do_odczytu.close()
        f_do_zapisu.close()