def SJF(kolejka):
    kolejka.sort(key=lambda x: x.czas_wykonania)
    return kolejka