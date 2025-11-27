# Есть суперкласс «Лекарство» — Medication. У него есть подкласс «Таблетка» — Tablet. 
# Создай в подклассе Tablet конструктор, вызови в нём конструктор суперкласса и добавь уникальный атрибут colour — цвет.


class Medication:
    def __init__(self, name, dosage):
        self.name = name
        self.dosage = dosage

    def consume(self):
        print(f"Принято лекарство - {self.name}. Доза - {self.dosage}")


class Tablet(Medication):
    # напиши конструктор, вызови в нём конструктор суперкласса и добавь новый атрибут colour
    def __init__(self, name, dosage, colour):
        Medication.__init__(self, name, dosage)
        self.colour = colour

    def print_colour(self):
        print(f"Цвет таблетки - {self.colour}")


tablet = Tablet("Наследин", "2", "Белый")
tablet.consume()       # Принято лекарство - Наследин. Доза - 2
tablet.print_colour()  # Цвет таблетки - Белый