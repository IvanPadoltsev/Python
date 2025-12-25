# Прочитать атрибуты объекта можно, а изменить — нет. Нужно это поправить. 
# Напиши сеттеры для приватных атрибутов. Новые значения в методах назови new_name, new_quantity и new_price. 
# В сеттер для атрибута price добавь условие:
# если цена продукта ниже 0, метод выводит сообщение "Цена не может быть отрицательной";
# если условие соблюдается, метод устанавливает новую цену.
# Код в конце программы вызовет сеттеры и напечатает новые значения переменных.


class Product:
    def __init__(self, name, quantity, price):
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    @property
    def name(self):
        return self.__name

    # напиши сеттер для свойства name
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def quantity(self):
        return self.__quantity

    # напиши сеттер для свойства quantity
    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity = new_quantity

    @property
    def price(self):
        return self.__price

    # напиши сеттер для свойства price
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            print("Цена не может быть отрицательной")
        else:
            self.__price = new_price

# тут программа создаст объект, вызовет сеттеры и выведет результат
product = Product("Яблоки", 0.6, 120)
product.name = "Апельсины"
product.quantity = 1.2
product.price = 240
print(product.name)
print(product.quantity)
print(product.price)