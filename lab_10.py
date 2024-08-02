from typing import Union, List

class Stos:
    def __init__(self, *args: Union[int, List[int], 'Stos']):
        """
        Inicjalizuje stos z przekazanymi parametrami.
        
        Args:
            *args: Elementy stosu, mogą być liczbami całkowitymi, listą lub innym obiektem klasy Stos.
        """
        if len(args) == 1:
            arg = args[0]
            if isinstance(arg, list):
                self.stos = list(arg)
            elif isinstance(arg, Stos):
                self.stos = list(arg.stos)
            else:
                raise TypeError("Argument powinien być listą lub obiektem klasy Stos.")
        else:
            self.stos = list(args)
    
    def dodaj_element(self, element: int) -> None:
        """
        Dodaje element do stosu.
        
        Args:
            element (int): Element do dodania.
        """
        if not isinstance(element, int):
            raise TypeError("Element musi być liczbą całkowitą.")
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
