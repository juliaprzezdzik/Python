import math
import itertools
import random

# 1. Generator nieskończony liczb naturalnych
def fun1():
    n = 0
    while True:
        yield n
        n += 1

# 2. Generator liczb doskonałych
def fun2(seq):
    def is_perfect(n):
        if n < 2:
            return False
        return sum(i for i in range(1, n) if n % i == 0) == n
    
    for number in seq:
        if is_perfect(number):
            yield number

# 3. Generator ograniczony przez wartość
def fun3(seq, limit):
    for value in seq:
        if value > limit:
            break
        yield value

# 4. Generator obliczający przybliżenie logarytmu naturalnego
def fun4(a):
    u = 0
    x = 1
    i = 0
    while x <= 1.5:
        yield x, u, math.log(x)
        u += a / x
        i += 1
        x = 1 + i * a

# 5. Generator przybliżający funkcję sinus
def fun5(x, tolerance=1e-8):
    k = 0
    term = x
    while abs(term) > tolerance:
        yield term
        k += 1
        term = ((-1)**k * x**(1 + 2 * k)) / math.factorial(1 + 2 * k)

# 6. Generator działający jak `range` dla liczb rzeczywistych
def fun6(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    current = start
    while (step > 0 and current < stop) or (step < 0 and current > stop):
        yield current
        current += step

# 7. Generator zwracający liczby spełniające warunek
def fun7():
    prev = random.uniform(0, 1)
    yield prev
    while True:
        curr = random.uniform(0, 1)
        if abs(curr - prev) >= 0.4:
            yield curr
            if curr < 0.1:
                break
        prev = curr

# Testowanie funkcji generatorowych

print("Perfect numbers less than 10000:")
for number in fun2(fun1()):
    if number >= 10000:
        break
    print(number)

print("\nLogarithm approximation:")
for x, approx, exact in fun4(0.05):
    print(f"x={x:.2f}, Approx={approx:.6f}, Exact={exact:.6f}")
    
print("\nSine approximation:")
x = math.pi / 4  # 45 degrees
for term in fun5(x):
    print(f"Term={term:.8f}")

print("\nCustom range generator:")
print(list(fun6(10)))
print(list(fun6(1, 10)))
print(list(fun6(10, 1, -2)))

print("\nRandom sequence generator:")
for number in fun7():
    print(number)
