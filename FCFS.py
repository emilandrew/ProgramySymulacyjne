def FCFS(kolejka):
    kolejka.sort(key=lambda x: x.czas_przyjscia)
    return kolejka