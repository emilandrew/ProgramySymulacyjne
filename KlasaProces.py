class Proces:
    def __init__(self, czas_przyjscia, czas_wykonania, czas_zakonczenia, czas_oczekiwania):
        self.czas_przyjscia = czas_przyjscia
        self.czas_wykonania = czas_wykonania
        self.czas_zakonczenia = czas_zakonczenia
        self.czas_oczekiwania = czas_oczekiwania

    def __repr__ (self):
        return f'Proces({self.czas_przyjscia},{self.czas_wykonania},{self.czas_zakonczenia},{self.czas_oczekiwania})'