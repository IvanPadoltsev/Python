# Вспомни пример из предыдущего урока с лекарствами. Есть суперкласс Medication и подклассы Tablet и Injection. Создай в подклассах конструкторы:
# вызови в подклассах конструктор суперкласса — используй super();
# для класса Tablet добавь уникальный атрибут colour — цвет;
# для класса Injection добавь уникальный атрибут needle_length — длина иглы.


class Medication:
    def __init__(self, name, dosage):
        self.name = name
        self.dosage = dosage

    def consume(self):
        print(f"Принято лекарство - {self.name}. Доза - {self.dosage}")


class Tablet(Medication):
    # напиши конструктор, используя super(), вызови в нём конструктор суперкласса
    # добавь новый атрибут colour
    def __init__(self, name, dosage, colour):
        super().__init__(name, dosage)
        self.colour = colour

    def print_colour(self):
        print(f"Цвет таблетки - {self.colour}")


class Injection(Medication):
    # напиши конструктор, используя super(), вызови в нём конструктор суперкласса
    # добавь новый атрибут needle_length
    def __init__(self, name, dosage, needle_length):
        super().__init__(name, dosage)
        self.needle_length = needle_length   

    def consume(self) -> None:
        print(f"Инъекция {self.name} сделана. Доза - {self.dosage}")

    def print_needle_length(self):
        print(f"Длина иглы - {self.needle_length}")


tablet = Tablet("Наследин", 2, "Белый")
tablet.consume()       # Принято лекарство - Наследин. Доза - 2
tablet.print_colour()  # Цвет таблетки - Белый
injection = Injection('ООПин', 1, "Средняя")
injection.consume()     # Инъекция ООПин сделана. Доза - 1
injection.print_needle_length()  # Длина иглы - Средняя