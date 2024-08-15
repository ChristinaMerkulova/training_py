def sum_numbers(*args):
    """Возвращает сум произвольного колва чисел."""
    return sum(args)


total = sum_numbers(1, 2, 3, 4, 5)
print(f"Сумма = {total}")
#формальные аргументы