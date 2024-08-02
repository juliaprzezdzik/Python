# 1. Usunięcie wszystkich wystąpień określonej wartości z listy (pętla `for`)
def fun1(lst, val):
    return [x for x in lst if x != val]

# 2. Usunięcie wszystkich wystąpień określonej wartości z listy (pętla `while`)
def fun2(lst, val):
    while val in lst:
        lst.remove(val)
    return lst

# 3. Wypisanie co drugiego elementu listy począwszy od indeksu 1 (pętla `for` oraz `range`)
def fun3(lst):
    for i in range(1, len(lst), 2):
        print(lst[i])

# 4. Wypisanie co drugiego elementu listy począwszy od indeksu 1 (bez `range`)
def fun4(lst):
    i = 1
    while i < len(lst):
        print(lst[i])
        i += 2

# 5. Wypisanie co drugiego elementu listy od końca (pętla `for` oraz `range`)
def fun5(lst):
    for i in range(len(lst) - 1, -1, -2):
        print(lst[i])

# 6. Wypisanie co drugiego elementu listy od końca (bez `range`)
def fun6(lst):
    i = len(lst) - 1
    while i >= 0:
        print(lst[i])
        i -= 2

# 7. Utworzenie nowej listy z krotkami (indeks, element) na podstawie istniejącej listy (lista składana)
def fun7(lst):
    return [(i, lst[i]) for i in range(len(lst))]

# 8. Posortowanie listy krotek wg drugiego elementu krotek
def fun8(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

# 9. Utworzenie nowej listy z krotkami (indeks, element) tylko dla wartości parzystych (lista składana)
def fun9(lst):
    return [(i, lst[i]) for i in range(len(lst)) if lst[i] % 2 == 0]

# 10. Utworzenie listy 2D wypełnionej zerami oraz jedynkami
def fun10(size):
    matrix = [[0] * size for _ in range(size)]
    
    # W kwadracie o boku mniejszym od rozmiaru listy na środku
    offset = size // 4
    for i in range(size // 2 - offset, size // 2 + offset):
        for j in range(size // 2 - offset, size // 2 + offset):
            matrix[i][j] = 1
    
    # Na przekątnej od lewego górnego rogu do prawego dolnego
    for i in range(size):
        matrix[i][i] = 1
    
    # Na przekątnej od prawego górnego rogu do lewego dolnego
    for i in range(size):
        matrix[i][size - 1 - i] = 1

    # W szachownicę
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                matrix[i][j] = 1

    return matrix

# Przykładowe użycia funkcji:

# 1. Usunięcie wartości z listy
my_list = [1, 2, 3, 4, 2, 5, 2]
value = 2
print("Usunięcie wartości (fun1):", fun1(my_list, value))
print("Usunięcie wartości (fun2):", fun2(my_list.copy(), value))

# 2. Wypisanie co drugiego elementu listy
my_list = [10, 20, 30, 40, 50, 60]
print("Co drugi element od indeksu 1 (fun3):")
fun3(my_list)
print("Co drugi element od indeksu 1 (fun4):")
fun4(my_list)

# 3. Wypisanie co drugiego elementu od końca
print("Co drugi element od końca (fun5):")
fun5(my_list)
print("Co drugi element od końca (fun6):")
fun6(my_list)

# 4. Krotki (indeks, element)
index_tuples = fun7(my_list)
print("Krotki (indeks, element) (fun7):", index_tuples)

# 5. Posortowane krotki wg drugiego elementu
sorted_tuples = fun8(index_tuples)
print("Posortowane krotki wg drugiego elementu (fun8):", sorted_tuples)

# 6. Krotki (indeks, element) tylko dla wartości parzystych
even_index_element_tuples = fun9(my_list)
print("Krotki (indeks, element) tylko dla wartości parzystych (fun9):", even_index_element_tuples)

# 7. Lista 2D
size = 5
matrix = fun10(size)
print("Lista 2D (fun10):")
for row in matrix:
    print(row)
