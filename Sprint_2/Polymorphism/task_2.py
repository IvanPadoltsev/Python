# Перед тобой модель экосистемы с классами Animal и Plant. 
# У класса Animal есть методы:
# move() — увеличивает счётчик distance_travelled, «пройденное расстояние»;
# eat() — увеличивает счётчик calories_consumed, «потребляемые калории».
# У класса Plant есть методы:
# grow() — увеличивает счётчик height, «рост»;
# photosynthesize() — увеличивает счётчик energy_stored, «накопленная энергия».
# Добавь в экосистему особое существо — класс ZombieHerbivore (зомби-травоядное). Это существо сочетает способности животного и растения. 
# Класс ZombieHerbivore использует множественное наследование от классов Animal и Plant и реализует все их методы. Переопределять их не нужно.


class Animal:
    distance_travelled = 0
    calories_consumed = 0

    def move(self):
        self.distance_travelled += 5
        return self.distance_travelled

    def eat(self):
        self.calories_consumed += 10
        return self.calories_consumed


class Plant:
    height = 0
    energy_stored = 0

    def grow(self):
        self.height += 1
        return self.height

    def photosynthesize(self):
        self.energy_stored += 10
        return self.energy_stored
    

# добавь класс ZombieHerbivore, который наследуется от Animal и Plant
class ZombieHerbivore(Animal, Plant):
    pass


# вызов методов для объекта класса ZombieHerbivore
zombie = ZombieHerbivore()
print(zombie.move())
print(zombie.eat())
print(zombie.grow())
print(zombie.photosynthesize())