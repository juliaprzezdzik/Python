import math

class Punkt:
    def __init__(self, x=0.0, y=0.0):
        """
        Inicjalizuje punkt z współrzędnymi x i y.
        
        Args:
            x (float): Współrzędna x punktu.
            y (float): Współrzędna y punktu.
        """
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value

def range_check(min_value, max_value):
    """
    Dekorator sprawdzający, czy wartości leżą w określonym zakresie.
    
    Args:
        min_value (float): Minimalna dozwolona wartość.
        max_value (float): Maksymalna dozwolona wartość.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not (min_value <= arg.x <= max_value and min_value <= arg.y <= max_value):
                    raise ValueError(f"Wartości współrzędnych są poza zakresem {min_value} do {max_value}.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@range_check(-100, 100)
def dodaj_punkty(punkt1, punkt2):
    """
    Dodaje dwa punkty.
    
    Args:
        punkt1 (Punkt): Pierwszy punkt.
        punkt2 (Punkt): Drugi punkt.
    
    Returns:
        Punkt: Nowy punkt będący sumą dwóch punktów.
    """
    return Punkt(punkt1.x + punkt2.x, punkt1.y + punkt2.y)

@range_check(-100, 100)
def odejmij_punkty(punkt1, punkt2):
    """
    Odejmuję drugi punkt od pierwszego.
    
    Args:
        punkt1 (Punkt): Pierwszy punkt.
        punkt2 (Punkt): Drugi punkt.
    
    Returns:
        Punkt: Nowy punkt będący różnicą dwóch punktów.
    """
    return Punkt(punkt1.x - punkt2.x, punkt1.y - punkt2.y)

class Geometria:
    @staticmethod
    def obwod_trojkata(a, b, c):
        """
        Oblicza obwód trójkąta.
        
        Args:
            a (float): Długość boku a.
            b (float): Długość boku b.
            c (float): Długość boku c.
        
        Returns:
            float: Obwód trójkąta.
        """
        return a + b + c
    
    @staticmethod
    def pole_trojkata(a, b, c):
        """
        Oblicza pole trójkąta za pomocą wzoru Herona.
        
        Args:
            a (float): Długość boku a.
            b (float): Długość boku b.
            c (float): Długość boku c.
        
        Returns:
            float: Pole trójkąta.
        """
        p = Geometria.obwod_trojkata(a, b, c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    @staticmethod
    def pole_czworokata(a, b, c, d):
        """
        Oblicza pole czworokąta wpisanego w okrąg za pomocą wzoru Brahmagupty.
        
        Args:
            a (float): Długość boku a.
            b (float): Długość boku b.
            c (float): Długość boku c.
            d (float): Długość boku d.
        
        Returns:
            float: Pole czworokąta.
        """
        p = (a + b + c + d) / 2
        return math.sqrt((p - a) * (p - b) * (p - c) * (p - d))

class CallCounter:
    counts = {}
    
    @staticmethod
    def count_calls(func):
        """
        Dekorator zliczający liczbę wywołań funkcji.
        
        Args:
            func (function): Funkcja do obliczenia liczby wywołań.
        
        Returns:
            wrapper: Funkcja opakowująca.
        """
        def wrapper(*args, **kwargs):
            if func.__name__ not in CallCounter.counts:
                CallCounter.counts[func.__name__] = 0
            CallCounter.counts[func.__name__] += 1
            return func(*args, **kwargs)
        return wrapper
    
    @staticmethod
    def get_counts():
        """
        Zwraca liczbę wywołań funkcji.
        
        Returns:
            dict: Słownik z liczbą wywołań funkcji.
        """
        return CallCounter.counts
