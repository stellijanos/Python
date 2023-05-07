# 3. Schreibe die folgende Funktion so um, dass sie rekursiv ist: (1p)
def my_func(n):
    lst = []
    total = 0
    for i in range(-n, n):
        if i % 10 == 0:
            total += i
        lst.append(total)
    return lst


def rekursiv(total, lista, start, end):
    if start < end:
        if start % 10 == 0:
            total += start
        lista.append(total)
        return rekursiv(total, lista, start + 1, end)
    return lista


n = 10
print(rekursiv(0, [], -n, n))
print(my_func(10))