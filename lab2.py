import sys
from collections import Counter

# 1. Utworzenie stringa z elementów listy argv (wyłączając nazwę programu)
def fun1(argv):
    if len(argv) <= 1:
        print("Usage: python script.py <string>")
        sys.exit(1)
    return ' '.join(argv[1:])

# 2. Utworzenie czterech list na podstawie stringa
def fun2(s):
    lower = [c for c in s if c.islower()]
    upper = [c for c in s if c.isupper()]
    nums = [c for c in s if c.isdigit()]
    others = [c for c in s if not c.isalpha()]
    return lower, upper, nums, others

# 3. Utworzenie listy małych liter bez powtórzeń (bez użycia set)
def fun3(lower):
    unique = []
    seen = []
    for c in lower:
        if c not in seen:
            seen.append(c)
            unique.append(c)
    return unique

# 4. Utworzenie listy krotek (litera, krotność jej wystąpienia) i posortowanie według krotności
def fun4(lower):
    counts = Counter(lower)
    counts_list = [(c, counts[c]) for c in counts]
    return sorted(counts_list, key=lambda x: x[1], reverse=True)

# 5. Utworzenie listy krotek (cyfra, wartość funkcji liniowej ax + b)
def fun5(digits, a, b):
    return [(int(d), a * int(d) + b) for d in digits]

# 6. Obliczanie współczynników a i b
def fun6(s):
    vowels = 'aeiou'
    num_vowels = sum(1 for c in s if c in vowels)
    num_consonants = sum(1 for c in s if c.isalpha() and c not in vowels)
    return num_vowels, num_consonants

def main():
    # 1. Pobranie stringa z argumentów
    s = fun1(sys.argv)
    
    # 2. Kategoryzowanie znaków
    lower, upper, nums, others = fun2(s)
    
    # 3. Unikalne małe litery
    unique_lower = fun3(lower)
    
    # 4. Krotki (litera, krotność)
    sorted_counts = fun4(lower)
    print("Krotki (litera, krotność) posortowane według krotności:", sorted_counts)
    
    # 5. Obliczanie współczynników a i b
    a, b = fun6(s)
    print(f"Współczynniki: a={a}, b={b}")
    
    # 6. Krotki (cyfra, wartość funkcji liniowej)
    lin_vals = fun5(nums, a, b)
    print("Krotki (cyfra, wartość funkcji liniowej):", lin_vals)

if __name__ == "__main__":
    main()
