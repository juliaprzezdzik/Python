import matplotlib.pyplot as plt
import numpy as np
import random
import math

class IFS:
    def __init__(self, transformations, probabilities):
        """
        Inicjalizuje obiekt IFS z danymi transformacjami i prawdopodobieństwami.
        
        Args:
            transformations (list of tuples): Lista krotek z współczynnikami przekształcenia.
            probabilities (list of floats): Lista prawdopodobieństw dla każdego przekształcenia.
        """
        self.transformations = transformations
        self.probabilities = probabilities
        self.point = (0, 0)
    
    def transform(self, iterations):
        """
        Przeprowadza iteracje przekształceń na punkcie startowym.
        
        Args:
            iterations (int): Liczba iteracji do przeprowadzenia.
        """
        x, y = self.point
        points = [(x, y)]
        
        for _ in range(iterations):
            # Wybór transformacji na podstawie prawdopodobieństw
            transformation = random.choices(self.transformations, self.probabilities)[0]
            a, b, c, d, e, f = transformation
            x, y = a * x + b * y + c, d * x + e * y + f
            points.append((x, y))
        
        self.points = points

    def plot(self):
        """
        Rysuje otrzymany wynik przekształceń.
        """
        if not hasattr(self, 'points'):
            raise RuntimeError("No points to plot. Run the 'transform' method first.")
        
        x_vals, y_vals = zip(*self.points)
        plt.figure(figsize=(8, 8))
        plt.plot(x_vals, y_vals, 'o', markersize=1, color='blue')
        plt.axis('equal')
        plt.title('IFS Fractal')
        plt.show()

class Wektor3D:
    def __init__(self, x, y, z):
        """
        Inicjalizuje wektor 3D.
        
        Args:
            x (float): Współrzędna x.
            y (float): Współrzędna y.
            z (float): Współrzędna z.
        """
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Wektor3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Wektor3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar):
        return Wektor3D(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __str__(self):
        return f"Wektor3D({self.x}, {self.y}, {self.z})"
    
    def length(self):
        """
        Zwraca długość wektora.
        
        Returns:
            float: Długość wektora.
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def dot(self, other):
        """
        Oblicza iloczyn skalarny z innym wektorem.
        
        Args:
            other (Wektor3D): Inny wektor.
            
        Returns:
            float: Iloczyn skalarny.
        """
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        """
        Oblicza iloczyn wektorowy z innym wektorem.
        
        Args:
            other (Wektor3D): Inny wektor.
            
        Returns:
            Wektor3D: Iloczyn wektorowy.
        """
        return Wektor3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def mixed(self, v, w):
        """
        Oblicza iloczyn mieszany z dwoma wektorami.
        
        Args:
            v (Wektor3D): Pierwszy wektor.
            w (Wektor3D): Drugi wektor.
            
        Returns:
            float: Iloczyn mieszany.
        """
        return self.dot(v.cross(w))

def magnetic_flux(B, S):
    """
    Oblicza strumień indukcji magnetycznej.
    
    Args:
        B (Wektor3D): Wektor indukcji magnetycznej.
        S (Wektor3D): Wektor pola powierzchni.
        
    Returns:
        float: Strumień indukcji magnetycznej.
    """
    return B.dot(S)

def lorentz_force(q, E, v, B):
    """
    Oblicza siłę Lorentza.
    
    Args:
        q (float): Ładunek.
        E (Wektor3D): Wektor pola elektrycznego.
        v (Wektor3D): Wektor prędkości.
        B (Wektor3D): Wektor indukcji magnetycznej.
        
    Returns:
        Wektor3D: Siła Lorentza.
    """
    return E * q + (v.cross(B) * q)

def work_of_lorentz(q, E, v):
    """
    Oblicza pracę siły Lorentza.
    
    Args:
        q (float): Ładunek.
        E (Wektor3D): Wektor pola elektrycznego.
        v (Wektor3D): Wektor prędkości.
        
    Returns:
        float: Praca siły Lorentza.
    """
    return q * E.dot(v)
