numbers = [1, 2, 3, 11, 21, 111, 231]

def sort(numbers):
    sorted_numbers = []
    while len(numbers) > 0:
        small = min(numbers)
        sorted_numbers.append(small)
        numbers.remove(smallest)

    return sorted_numbers

print(sort(numbers))
