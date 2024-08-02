import random
import string

# 1. Utworzenie k-elementowej listy całkowitych wartości losowych z przedziału [0, 5k)
def fun1(k):
    return [random.randint(0, 5 * k - 1) for _ in range(k)]

# 2. Sprawdzenie ile elementów pozostaje na swoim miejscu po losowym przemieszaniu listy
def fun2(k, trials=100):
    original_list = fun1(k)
    fixed_counts = {}
    
    for _ in range(trials):
        shuffled_list = original_list[:]
        random.shuffle(shuffled_list)
        fixed_positions = sum(1 for i in range(k) if shuffled_list[i] == original_list[i])
        fixed_counts[fixed_positions] = fixed_counts.get(fixed_positions, 0) + 1
    
    return fixed_counts

# 3. Utworzenie losowego stringa o długości k z małych liter z kropkami
def fun3(k):
    return '.'.join(random.choices(string.ascii_lowercase, k=k))

# 4. Utworzenie słownika z listy losowych wartości, klucze to liczby, wartości to ich indeksy (metoda setdefault i enumerate)
def fun4():
    lst = [random.randint(0, 19) for _ in range(100)]
    d = {}
    for idx, num in enumerate(lst):
        d.setdefault(num, []).append(idx)
    return d

# 5. Utworzenie słownika z listy losowych wartości, klucze to liczby, wartości to ich indeksy (metoda setdefault i index)
def fun5():
    lst = [random.randint(0, 19) for _ in range(100)]
    d = {}
    for num in lst:
        d.setdefault(num, []).append(lst.index(num))
    return d

# 6. Sprawdzenie liczby palindromów w 1000 losowych liczbach o długości od 3 do 6 cyfr
def fun6(num_count=1000):
    def is_palindrome(s):
        return s == s[::-1]
    
    pal_count = {}
    for _ in range(num_count):
        n = random.randint(100, 999999)
        s = str(n)
        if 3 <= len(s) <= 6:
            key = len(s)
            if is_palindrome(s):
                pal_count[key] = pal_count.get(key, 0) + 1
    
    return pal_count

# 7. Zamiana kluczy z wartościami w dwóch słownikach i tworzenie nowego słownika z krotkami
def fun7():
    d1 = {i: random.randint(1, 100) for i in range(1, 11)}
    d2 = {i: random.randint(1, 100) for i in range(1, 11)}
    
    d1_swapped = {v: k for k, v in d1.items()}
    d2_swapped = {v: k for k, v in d2.items()}
    
    common_keys = set(d1_swapped.keys()) & set(d2_swapped.keys())
    
    result = {key: (d1[d1_swapped[key]], d2[d2_swapped[key]]) for key in common_keys}
    
    return result

# Przykładowe użycia funkcji:
if __name__ == "__main__":
    # 1. Generowanie i wypisywanie listy
    k = 10
    random_list = fun1(k)
    print("Losowa lista:", random_list)
    
    # 2. Sprawdzenie liczby elementów pozostających na miejscu
    fixed_positions = fun2(k)
    print("Liczba stałych pozycji:", fixed_positions)
    
    # 3. Generowanie losowego stringa z kropkami
    rand_str = fun3(k)
    print("Losowy string z kropkami:", rand_str)
    
    # 4. Słownik z metodą setdefault i enumerate
    dict_with_enumerate = fun4()
    print("Słownik z enumerate:", dict_with_enumerate)
    
    # 5. Słownik z metodą setdefault i index
    dict_no_enumerate = fun5()
    print("Słownik bez enumerate:", dict_no_enumerate)
    
    # 6. Liczba palindromów
    palindrome_counts = fun6()
    print("Liczba palindromów:", palindrome_counts)
    
    # 7. Nowy słownik po zamianie kluczy i wartości
    new_dict = fun7()
    print("Nowy słownik z krotkami:", new_dict)
