from functools import reduce
"""
    Возвращает произведение чисел в списке.
    Если список пуст, возвращает 1.
"""


def multiply(list):
    return reduce(lambda x, y: x * y, list)

s = [1, 2, 3, 4]
res = multiply(s)
print(res)
