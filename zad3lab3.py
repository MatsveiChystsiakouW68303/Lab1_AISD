numbers = [1, 2, 3, 11, 21, 111, 231]

strings = [str(n) for n in numbers]
strings.sort()
sorted_numbers = [int(s) for s in strings]

print(sorted_numbers)
