# Класс Person описывает обычного человека. Метод introduce() выводит его приветствие.
# В подклассе SpiderMan нужно переопределить метод introduce(), который печатает строчку "Но вы можете знать меня как Человека-паука.", если аргумент with_identity=True. 
# Используй super(), чтобы взять метод суперкласса и добавить ему настройки.


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}.")


class SpiderMan(Person):
    def __init__(self, name):
        super().__init__(name)

    def introduce(self, with_identity=False):
    # переопредели метод суперкласса, используя super()
    # добавь новое условие, используя with_identity
        if with_identity:
            super().introduce()
            print(f"Но вы можете знать меня как Человека-паука.")
        else:
            super().introduce()


peter = SpiderMan("Питер Паркер")
peter.introduce(with_identity=True)  
# Привет, меня зовут Питер Паркер. 
# Но вы можете знать меня как Человека-паука.