# Есть суперкласс Tester. Что тебе нужно сделать:
# Создай подкласс Autotester. Его конструктор принимает параметры name — имя и tool — инструмент, с помощью которого автоматизатор работает.
# Используй функцию super() для вызова метода __init__() суперкласса, чтобы инициализировать имя тестера.
# В конструкторе Autotester инициализируй атрибут self.tool с помощью переданного аргумента tool.
# Переопредели метод test в классе Autotester так, чтобы он возвращал строку «Автотестировщик <имя> проводит тестирование с помощью <название инструмента>».
# Создай по одному объекту для каждого класса: Tester и Autotester.
# Для объекта Tester в качестве имени используй Иван, а для объекта Autotester — Маша и инструмент Selenium.
# Вызови метод test() для каждого из объектов и распечатай результат.


class Tester:
    def __init__(self, name):
        self.name = name

    def test(self):
        return f"Тестировщик {self.name} проводит тестирование"

# допиши свой код здесь
class Autotester(Tester):
    def __init__(self, name, tool):
        super().__init__(name)
        self.tool = tool

    def test(self):
        return f"Автотестировщик {self.name} проводит тестирование с помощью {self.tool}"
    

tester = Tester("Иван")
tester.test()

autotester = Autotester("Маша", "Selenium")
autotester.test()

print(tester.test())
print(autotester.test())