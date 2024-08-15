def remove_spaces(strings):
    """
    Удаляет пробелы в начале и конце каждой строки в списке
    strings (list): Список строк
    Возвращает новый список строк с удаленными пробелами
    """
    return [s.strip() for s in strings]  #Удаляем пробелы


old_strings = [" hello ", "world ", " python", "computer science"]
new_strings = remove_spaces(old_strings)
print(new_strings)  #'hello', 'world', 'python', 'computer science'