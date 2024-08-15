def stroka(s):

    d = "" #пустая строка для хран

    for c in s: #проходимся по всем символам
        if c.isdigit(): #цифра или нет
            d += c #если да - добавляем в пустую d

    return d #возвращ


vveli = "gfkjhg78dssd68!23"
result = stroka(vveli)
print(result) #должно получ 786823