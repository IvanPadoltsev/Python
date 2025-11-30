# Создай суперкласс и два подкласса, в которых ты переопределишь метод.
# Создай класс Animal. В нём есть:
# Атрибут energy. Он показывает текущую энергию животного.
# Метод make_sound(), который снижает энергию животного на 5 единиц при каждом вызове. Не забудь сделать return текущей энергии после снижения.
# Создай класс Dog, который наследуется от Animal. Переопредели метод make_sound() так, чтобы при его вызове печаталось "Гав" и энергия снижалась на 10 единиц, а не на 5.
# Создай класс Cat, который также наследуется от Animal. Переопредели метод make_sound() так, чтобы при его вызове печаталось "Мяу" и энергия снижалась только на 2 единицы.


class Animal:
    def __init__(self, energy):
        self.energy = energy

    def make_sound(self):
        self.energy -= 5  # каждый звук требует 5 единицы энергии

        return self.energy


class Dog(Animal):

    def make_sound(self):
        print("Гав")
        self.energy -= 10  # каждый Гав требует 10 единицы энергии

        return self.energy
    

class Cat(Animal):

    def make_sound(self):
        print("Мяу")
        self.energy -= 2  # каждый Мяу требует 5 единицы энергии

        return self.energy


... # создай классы Animal, Dog и Cat, в каждом из которых будет метод make_sound

# пример использования
animal = Animal(100)
print(animal.make_sound())  # вывод: 95

dog = Dog(100)
print(dog.make_sound())  # вывод: "Гав" 90

cat = Cat(100)
print(cat.make_sound())  # вывод: "Мяу" 98