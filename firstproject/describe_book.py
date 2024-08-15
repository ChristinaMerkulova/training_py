def describe_book(title, author = "Неизвестный автор", **kwargs):
    """Выводит информацию о книге."""
    print(f"Название: {title}")
    print(f"Автор: {author}")

    # Выводим дополнительные данные, если они есть
    for key, value in kwargs.items():
        print(f"{value}")


describe_book("Исповедь", "Аврелий Августин", year="397-398 до н.э.", genre="Автобиография", pages=400)

describe_book("Мастер и Маргарита")  # Используем значение по умолчанию