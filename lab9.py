import json
import os
import random
import dataclasses
from typing import List, Union, Any

# 1. **Klasa Stos**

class Stos:
    def __init__(self, *args: Union[int, List[int], 'Stos']):
        """
        Inicjalizuje stos z przekazanymi parametrami.
        
        Args:
            *args: Elementy stosu, mogą być liczbami całkowitymi, listą lub innym obiektem klasy Stos.
        """
        match args:
            case [list() as lst]:
                self.stos = lst
            case [Stos() as other_stos]:
                self.stos = other_stos.stos.copy()
            case _:
                self.stos = list(args)
    
    def dodaj_element(self, element: int) -> None:
        """
        Dodaje element do stosu.
        
        Args:
            element (int): Element do dodania.
        """
        self.stos.append(element)
    
    def wypisz_stos(self) -> None:
        """
        Wypisuje elementy stosu.
        """
        print(self.stos)

# Testowanie klasy Stos
s1 = Stos(1, 2, 3)
s2 = Stos([4, 5, 6])
s3 = Stos(s1)

s1.dodaj_element(7)
s2.dodaj_element(8)
s3.dodaj_element(9)

s1.wypisz_stos()  # Oczekiwane: [1, 2, 3, 7]
s2.wypisz_stos()  # Oczekiwane: [4, 5, 6, 8]
s3.wypisz_stos()  # Oczekiwane: [1, 2, 3, 7, 9]

# 2. **Klasa StosPosortowany**

class StosPosortowany(Stos):
    def __init__(self, *args: Union[int, List[int], 'Stos']):
        """
        Inicjalizuje posortowany stos.
        
        Args:
            *args: Elementy stosu, mogą być liczbami całkowitymi, listą lub innym obiektem klasy Stos.
        """
        super().__init__(*args)
        self.stos.sort()
        self.typ = self._dominant_type()

    def _dominant_type(self) -> type:
        """
        Określa typ elementów najliczniej reprezentowanych w stosie.
        
        Returns:
            type: Typ najliczniej reprezentowanych elementów.
        """
        types = {}
        for element in self.stos:
            t = type(element)
            if t not in types:
                types[t] = 0
            types[t] += 1
        return max(types, key=types.get)

    def dodaj_element(self, element: int) -> None:
        """
        Dodaje element do posortowanego stosu, zachowując porządek.
        
        Args:
            element (int): Element do dodania.
        """
        if type(element) == self.typ:
            self.stos.append(element)
            self.stos.sort()

    def _get_average_size(self, n: int) -> float:
        """
        Oblicza średni rozmiar posortowanego stosu.
        
        Args:
            n (int): Liczba prób.
        
        Returns:
            float: Średni rozmiar posortowanego stosu.
        """
        sizes = []
        for _ in range(n):
            self.stos = [random.randint(0, 100) for _ in range(100)]
            self.stos.sort()
            sizes.append(len(self.stos))
        return sum(sizes) / len(sizes)

# Testowanie klasy StosPosortowany
sp = StosPosortowany(3, 1, 4, 1, 5)
sp.dodaj_element(2)
sp.dodaj_element(6)
sp.wypisz_stos()  # Oczekiwane: posortowane elementy [1, 1, 2, 3, 4, 5, 6]

# Średni rozmiar posortowanego stosu
print("Średni rozmiar posortowanego stosu:", sp._get_average_size(100))

# 3. **Klasy z Dekoratorem @dataclass**

@dataclass
class Pracownik:
    nazwisko: str
    wiek: int
    wykształcenie: str

@dataclass
class OfertaPracy:
    opis: str
    wiek: int
    wykształcenie: str

class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)

def wczytaj_bazy(pracownicy_file: str, oferty_file: str) -> (List[Pracownik], List[OfertaPracy]):
    """
    Wczytuje bazy pracowników i ofert pracy z plików JSON.
    
    Args:
        pracownicy_file (str): Ścieżka do pliku JSON z pracownikami.
        oferty_file (str): Ścieżka do pliku JSON z ofertami pracy.
    
    Returns:
        tuple: Lista pracowników i lista ofert pracy.
    """
    pracownicy = []
    oferty = []
    
    if os.path.isfile(pracownicy_file):
        with open(pracownicy_file, 'r') as f:
            pracownicy = json.load(f, object_hook=lambda d: Pracownik(**d))
    
    if os.path.isfile(oferty_file):
        with open(oferty_file, 'r') as f:
            oferty = json.load(f, object_hook=lambda d: OfertaPracy(**d))
    
    return pracownicy, oferty

def zapisz_bazy(pracownicy: List[Pracownik], oferty: List[OfertaPracy], pracownicy_file: str, oferty_file: str) -> None:
    """
    Zapisuje bazy pracowników i ofert pracy do plików JSON.
    
    Args:
        pracownicy (List[Pracownik]): Lista pracowników.
        oferty (List[OfertaPracy]): Lista ofert pracy.
        pracownicy_file (str): Ścieżka do pliku JSON z pracownikami.
        oferty_file (str): Ścieżka do pliku JSON z ofertami pracy.
    """
    with open(pracownicy_file, 'w') as f:
        json.dump(pracownicy, f, cls=EnhancedJSONEncoder, indent=4)
    
    with open(oferty_file, 'w') as f:
        json.dump(oferty, f, cls=EnhancedJSONEncoder, indent=4)

def wyszukaj_oferty(pracownik: Pracownik, oferty: List[OfertaPracy]) -> List[OfertaPracy]:
    """
    Wyszukuje oferty pracy pasujące do danego pracownika.
    
    Args:
        pracownik (Pracownik): Obiekt pracownika.
        oferty (List[OfertaPracy]): Lista ofert pracy.
    
    Returns:
        List[OfertaPracy]: Lista ofert pracy pasujących do pracownika.
    """
    return [
        oferta for oferta in oferty
        if pracownik.wiek >= oferta.wiek and pracownik.wykształcenie == oferta.wykształcenie
    ]

# Testowanie funkcji
pracownicy, oferty = wczytaj_bazy('pracownicy.json', 'oferty.json')
nowy_pracownik = Pracownik("Nowak", 30, "Wyższe")
oferty_pasujace = wyszukaj_oferty(nowy_pracownik, oferty)
print(oferty_pasujace)
