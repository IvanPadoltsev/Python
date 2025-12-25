# Перед тобой класс Circle. У него есть приватный атрибут «радиус» — __radius. Значение радиуса задаётся при инициализации объекта класса.
# Сделай приватный атрибут свойством:
# Напиши для radius геттер с декоратором @property;
# Вызови геттер внутри функцииprint() и напечатай радиус объекта circle.


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    # создай геттер для свойства radius
    @property
    def radius(self):
        return self.__radius

circle = Circle(5)
print(circle.radius)  # вызови геттер у объекта circle для свойства radius
