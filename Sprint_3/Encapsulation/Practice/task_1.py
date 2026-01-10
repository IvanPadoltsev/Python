# Ты будешь работать с классом Product. Он хранит данные о товарах на складе.
# У каждого товара есть:
# name — название;
# quantity — количество;
# price — цена за единицу.
# Задай эти атрибуты через конструктор.


class Product:
    def __init__(self, name, quantity, price):
    # допиши атрибуты
        self.name = name
        self.quantity = quantity
        self.price = price