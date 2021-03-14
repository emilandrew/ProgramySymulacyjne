from FCFS import *
from SJF import *
from GeneratorDanych import *


##################################

def symulacja_procesora ():
    i = 0
    licznik = 0
    kolejka = []
    var = 0
    sredni_czas_oczekiwania_procesu = 0

    while i < 40000:

        for p in procesy:
            if i >= p.czas_przyjscia and p not in kolejka:
                kolejka.append(p)
                #print(str(p) + " zostal dodany do kolejki")

                #kolejka = FCFS(kolejka) # kolejka posortowana wzgledem algorytmu FCFS
                kolejka = SJF(kolejka) # kolejka posortowana wzgledem algorytmu SJF

        if len(kolejka) > var:
            czas_wykonania_bufor = kolejka[licznik].czas_wykonania
            while kolejka[licznik].czas_wykonania != 0:
                kolejka[licznik].czas_wykonania -= 1
                #print(i)
                i += 1

            kolejka[licznik].czas_zakonczenia = i
            #print(str(kolejka[licznik]) + " zostal zakonczony w momencie " + str(i))
            kolejka[licznik].czas_oczekiwania = kolejka[licznik].czas_zakonczenia - czas_wykonania_bufor
            licznik += 1
            var += 1
            i -= 1

        i += 1

    suma_czasow_oczekiwania = 0
    # Obliczanie sumy czasow oczekiwania
    for k in kolejka:
        suma_czasow_oczekiwania += k.czas_oczekiwania
        #print(k.czas_oczekiwania)

    # Obliczanie sredniego czasu oczekiwania
    sredni_czas_oczekiwania_procesu = suma_czasow_oczekiwania / ilosc_procesow

    # Obliczanie odchylenia standardowego
    gora_rownania = 0
    for p in kolejka:
        gora_rownania += (p.czas_oczekiwania - sredni_czas_oczekiwania_procesu)**2

    wartosc_pod_pierwiastkiem = gora_rownania / ilosc_procesow
    odchylenie_standardowe = wartosc_pod_pierwiastkiem**(1/2)

    #####################################

    print("Sredni czas oczekiwania procesu: " + str(sredni_czas_oczekiwania_procesu))
    print("Odchylenie standardowe czasow oczekiwania: " + str(odchylenie_standardowe))
##################################

procesy = []

generator_danych(procesy)

symulacja_procesora()
