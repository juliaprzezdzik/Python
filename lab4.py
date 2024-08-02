import random
import sys
from collections import Counter

# FUN1 - Utworzenie stringa z elementów listy argv (wyłączając nazwę programu)
def fun1(argv):
    if len(argv) <= 1:
        print("Usage: python script.py <string>")
        sys.exit(1)
    return ' '.join(argv[1:])

# FUN2 - Utworzenie czterech list na podstawie stringa
def fun2(s):
    lowercase = [char for char in s if char.islower()]
    uppercase = [char for char in s if char.isupper()]
    digits = [char for char in s if char.isdigit()]
    non_letters = [char for char in s if not char.isalpha()]
    return lowercase, uppercase, digits, non_letters

# FUN3 - Utworzenie listy małych liter bez powtórzeń (bez użycia set)
def fun3(lowercase_letters):
    unique_letters = []
    seen = []
    for char in lowercase_letters:
        if char not in seen:
            seen.append(char)
            unique_letters.append(char)
    return unique_letters

# FUN4 - Utworzenie listy krotek (litera, krotność jej wystąpienia) i posortowanie według krotności
def fun4(lowercase_letters):
    counts = Counter(lowercase_letters)
    letter_counts = [(char, counts[char]) for char in counts]
    sorted_by_count = sorted(letter_counts, key=lambda x: x[1], reverse=True)
    return sorted_by_count

# FUN5 - Utworzenie listy krotek (cyfra, wartość funkcji liniowej)
def fun5(digits, a, b):
    return [(int(digit), a * int(digit) + b) for digit in digits]

# FUN6 - Funkcja do generowania wartości a i b
def fun6(s):
    vowels = 'aeiou'
    num_vowels = sum(1 for char in s if char in vowels)
    num_consonants = sum(1 for char in s if char.isalpha() and char not in vowels)
    return num_vowels, num_consonants

# FUN7 - Funkcja do generowania listy dwuelementowych krotek (x, f(x)) z losowymi wartościami stałych
def fun7(expr):
    constants = {c: random.randint(0, 9) for c in 'abcdefghijklmnopqrstuvwxyz'}
    translation_table = str.maketrans(''.join(constants.keys()), ''.join(str(constants[c]) for c in constants.keys()))
    translated_expr = expr.translate(translation_table)
    func = lambda x: eval(translated_expr)
    return [(x, func(x)) for x in [random.random() for _ in range(10)]]

# FUN8 - Funkcja przyjmująca zmienną liczbę parametrów i zwracająca listę wspólnych elementów
def fun8(*args):
    common = set(args[0])
    for arg in args[1:]:
        common &= set(arg)
    return list(common)

# FUN9 - Funkcja zwracająca listę dwuelementowych krotek z sekwencji
def fun9(seq1, seq2, truncate=True):
    return [(seq1[i], seq2[i]) for i in range(min(len(seq1), len(seq2)))] if truncate else \
           [(seq1[i] if i < len(seq1) else None, seq2[i] if i < len(seq2) else None) for i in range(max(len(seq1), len(seq2)))]

# FUN10 - Funkcja rozmieniania kwoty pieniędzy
def fun10(amount, denominations=(10, 5, 2)):
    result = []
    for denom in sorted(denominations, reverse=True):
        count, amount = divmod(amount, denom)
        result.append((denom, count))
    return result

# FUN11 - Funkcja zgadywania liczby z przedziału
def fun11(target, low, high, method='r'):
    steps = 0
    while low <= high:
        steps += 1
        if method == 'r':
            guess = random.randint(low, high)
        elif method == 'b':
            guess = (low + high) // 2
        
        if guess == target:
            return steps
        elif guess < target:
            low = guess + 1
        else:
            high = guess - 1
    
    return steps

# Przykładowe użycia funkcji:

# FUN1
argv = ['script.py', 'a', 'b', 'c']
print("FUN1:", fun1(argv))

# FUN2
input_string = 'Hello World 123!'
lowercase, uppercase, digits, non_letters = fun2(input_string)
print("FUN2:", lowercase, uppercase, digits, non_letters)

# FUN3
print("FUN3:", fun3(lowercase))

# FUN4
print("FUN4:", fun4(lowercase))

# FUN5
a, b = fun6(input_string)
print("FUN5:", fun5(digits, a, b))

# FUN7
expr = 'a*x**2 + b*x + c'
print("FUN7:", fun7(expr))

# FUN8
print("FUN8:", fun8([1,2,3], (1,3,5), [3,2]))
print("FUN8:", fun8([1,2,3], (1,3,5), [3,2,1]))

# FUN9
print("FUN9:", fun9([1, 2, 3], ['a', 'b']))
print("FUN9:", fun9([1, 2, 3], ['a', 'b'], truncate=False))

# FUN10
print("FUN10:", fun10(32))
print("FUN10:", fun10(32, denominations=(7, 3, 1)))

# FUN11
print("FUN11 (random guessing):", fun11(45, 0, 100))
print("FUN11 (binary search):", fun11(45, 0, 100, 'b'))
