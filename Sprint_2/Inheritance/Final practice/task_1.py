# Создай класс Species — вид сущностей в нашей модели экосистемы. В его конструкторе задаются атрибуты:
# population — население (число),
# growth_rate — скорость роста (число).
# Добавь метод grow(). Он увеличивает численность вида на основе его текущего размера и скорости роста. Другими словами, population увеличивается на population * growth_rate.
# Посмотри, как изменяется популяция в зависимости от скорости роста: распечатай значение атрибута population до и после вызова метода grow() для экземпляра класса Species.


# для класса Species реализуй конструктор и метод grow()
class Species:
    def __init__(self, population, growth_rate):
        self.population = population
        self.growth_rate = growth_rate

    def grow(self):
        self.population += self.population * self.growth_rate
        return self.population


species = Species(1000, 0.02)
print(species.population)
species.grow()
print(species.population)