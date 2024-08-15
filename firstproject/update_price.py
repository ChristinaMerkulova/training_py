def update_price(old_prices):
    """
    Обновляет список старых цен, увеличивая каждую цену на 10%
    old_prices (list): Список старых цен (числа)
    Возвращает список новых цен, округленных до 2 знаков после запятой
    """
    new_prices = []  # Список для хранения новых цен

    for price in old_prices:
        new_price = price + price * 0.1  # Цена + 10%
        new_prices.append(round(new_price, 2))  # Округляем и добавляем

    return new_prices


old_prices = [100, 200, 300, 400]  # Старые цены
new_prices = update_price(old_prices)  # Новые цены
print(new_prices)  # Вывод: [110.0, 220.0, 330.0, 440.0]