liczby = [4, 8, 23, 1, 1, 45, 276]
def sort(liczby):
    strings = [str(n) for n in liczby]
    strings.sort()
    sorted = [int(s) for s in strings]
    return sorted
print(sort(liczby))
