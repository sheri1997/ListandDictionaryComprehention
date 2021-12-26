"""Practise Problem On Dictionary Comprehension
    Printing Power of First 10 Numbers"""


def dictionary_comprehension():
    power = {x: x ** 2 for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
    return power


value = dictionary_comprehension()
print(value)
