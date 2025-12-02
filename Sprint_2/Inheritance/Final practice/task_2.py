# Класс Species есть, время создавать подклассы.
# Создай класс Predator — хищник. Он наследуется от Species. 
# В конструкторе класса Predator задаётся дополнительный атрибут hunting_success_rate — коэффициент успешности охоты (число). Он влияет на уровень выживаемости вида.
# Атрибуты population и growth_rate наследуй от Species.
# Добавь хищникам метод survive(). Он уменьшает популяцию в зависимости от hunting_success_rate: чем коэффициент меньше, тем больше особей гибнет. 
# Другими словами, population уменьшается на произведение population и (1 - hunting_success_rate).
# Посмотри, как изменяется популяция в зависимости от коэффициента успешности охоты: распечатай значение атрибута population до и после вызова метода survive() для экземпляра класса Predator.


class Species:
    def __init__(self, population, growth_rate):
        self.population = population
        self.growth_rate = growth_rate

    def grow(self):
        self.population += self.population * self.growth_rate


# наследуй класс Predator от Species, реализуй конструктор и метод survive()
class Predator(Species):
    def __init__(self, population, growth_rate, hunting_success_rate):
        super().__init__(population, growth_rate)
        self.hunting_success_rate = hunting_success_rate

    def survive(self):
        self.population -= self.population * (1 - self.hunting_success_rate)


predator = Predator(1000, 0.02, 1.05)
print(predator.population)
predator.survive()
print(predator.population)