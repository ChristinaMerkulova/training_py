old_prices = [100, 200, 300, 400]

new_prices = list(map(lambda price: round(price + price * 0.1, 2), old_prices))

print(new_prices)