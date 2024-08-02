import random
import math
import time
from functools import reduce

# Pomocnicza funkcja do pomiaru czasu
def tester(func):
    start_time = time.time_ns()
    for _ in range(1000):
        func()
    end_time = time.time_ns()
    return (end_time - start_time) / 1000

# Funkcje budujące zestaw wartości różnymi metodami

def fun1():
    result = []
    for i in range(10000):
        result.append(i)

def fun2():
    result = [i for i in range(10000)]

def fun3():
    result = list(map(lambda x: x, range(10000)))

def fun4():
    result = list(x for x in range(10000))

# Testowanie funkcji
print(sys.version)
test_functions = [fun1, fun2, fun3, fun4]
for testFunction in test_functions:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

# Funkcja Monte-Carlo do oszacowania liczby pi
def estimate_pi(num_points=10000):
    inside_circle = lambda point: point[0]**2 + point[1]**2 <= 1
    points = [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(num_points)]
    count_inside = len(list(filter(inside_circle, points)))
    return 4 * count_inside / num_points

print("Estimated Pi:", estimate_pi())

# Funkcja do obliczania współczynników prostej i ich niepewności
def linear_regression(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(map(lambda xi, yi: xi * yi, x, y))
    sum_x2 = sum(map(lambda xi: xi ** 2, x))

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    b = (sum_y - a * sum_x) / n

    sxx = sum_x2 - (sum_x ** 2) / n
    syy = sum(map(lambda yi: yi ** 2, y)) - (sum_y ** 2) / n
    sxy = sum_xy - (sum_x * sum_y) / n

    s = math.sqrt((syy - a * sxy) / (n - 2))
    se_a = s / math.sqrt(sxx)
    se_b = s * math.sqrt(sum(xi ** 2 for xi in x) / (n * sxx))
    
    return a, b, se_a, se_b

# Funkcja myreduce
def myreduce(func, sequence):
    return reduce(func, sequence)

# Przykłady użycia myreduce
print("myreduce (addition):", myreduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
print("myreduce (multiplication):", myreduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))

# Macierz do operacji
matrix = [[random.randint(1, 100) for _ in range(5)] for _ in range(4)]

# Największa wartość w każdym wierszu
max_in_rows = list(map(max, matrix))
print("Max in each row:", max_in_rows)

# Największa wartość w każdej kolumnie
max_in_columns = list(map(max, zip(*matrix)))
print("Max in each column:", max_in_columns)

# Suma wszystkich elementów macierzy
matrix_sum = sum(sum(row) for row in matrix)
print("Sum of all elements in matrix:", matrix_sum)
