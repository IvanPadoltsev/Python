# Хищник есть, нужно создать травоядных.
# Создай класс Herbivore — травоядное. Он также наследуется от Species. У класса Herbivore должен быть дополнительный атрибут food_availability — доступность пищи. 
# Он задаётся в конструкторе класса и принимает значения от 0 до 1.
# Переопредели метод grow(), чтобы он учитывал доступность пищи:
# Если доступность пищи больше 0.2, популяция увеличивается в соответствии со скоростью роста growth_rate, а доступность пищи уменьшается на 0.15.
# Если food_availability становится меньше или равно 0.2, вызывается метод migrate(). Метод migrate() симулирует миграцию травоядных в поисках новых пастбищ. 
# При миграции погибает 20 % популяции, а доступность пищи сбрасывается до 0.3.
# Посмотри, как изменяется популяция в зависимости от уменьшения доступности пищи: 
# распечатай значения атрибутов population и food_availability после двух вызовов метода grow() для экземпляра класса Herbivore.


class Species:
    def __init__(self, population, growth_rate):
        self.population = population
        self.growth_rate = growth_rate

    def grow(self):
        self.population += self.population * self.growth_rate


# наследуй класс Herbivore от Species, реализуй конструктор и 
# переопредели метод grow()
class Herbivore(Species):
    def __init__(self, population, growth_rate, food_availability):
        super().__init__(population, growth_rate)
        self.food_availability = food_availability

    def grow(self):
        if self.food_availability >= 0.2:
            self.population += self.growth_rate
            self.food_availability -= 0.15
        elif self.food_availability <= 0.2:
            Herbivore.migrate(self)

    def migrate(self):
        self.population -= 0.2 * self.population
        self.food_availability = 0.3


herbivore = Herbivore(2000, 0.04, 0.3)
herbivore.grow()
print(herbivore.population)
print(herbivore.food_availability)
herbivore.grow()
print(herbivore.population)
print(herbivore.food_availability)