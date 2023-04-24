liczby = [1, 2, 3, 11, 21, 111, 231]

def sort1(numbers):
    sorted_numbers = []
    while len(numbers) > 0:
        small = min(lizcby)
        sorted_numbers.append(small)
        numbers.remove(small)

    return sorted_numbers

print(sort(liczby))
