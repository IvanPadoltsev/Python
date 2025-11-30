# Есть класс Animal и два его подкласса: Dog и Cat. 
# Класс CatDog пытается наследоваться от Animal, Dog и Cat. Хочется, чтобы CatDog мог использовать уникальные методы обоих классов. 
# Но из-за текущего порядка наследования это невозможно. 
# Исправь и доработай код:
# В классе CatDog убери наследование от класса Animal. Это лишнее, потому что классы Dog и Cat уже наследуются от него.
# Добавь в класс CatDog свой метод sound(), который выводит Мяу! Гав!. Для этого:
# Вызови метод sound() из класса Cat. Помни, что в множественном наследовании не нужно использовать super(): обращайся через имя суперкласса.
# Добавь к результату пробел: ' '.
# Добавь к результату вызов метода sound() из класса Dog.


class Animal:
    def sound(self):
        return "тихое молчание"


class Dog(Animal):
    def sound(self):
        return "Гав!"


class Cat(Animal):
    def sound(self):
        return "Мяу!"


class CatDog(Dog, Cat):
    def sound(self):
        return Cat.sound(self) + " " + Dog.sound(self)

my_pet = CatDog()
print(my_pet.sound())
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases Animal, Dog, Cat