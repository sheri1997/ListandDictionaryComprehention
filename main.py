"""Practise Problem On List Comprehension
    Printing Table Of Any Number"""


def list_comprehension(number):
    table = [i * number for i in range(1, 11)]
    return table


value = int(input("Enter The Number Whose Table You Want To Print : "))
table_value = list_comprehension(value)
print(table_value)

