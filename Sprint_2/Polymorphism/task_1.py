# Потренируйся с переопределением напоследок. Созданы два класса, Car и Bicycle, каждый из которых имеет метод calculate_travel_time(). 
# Метод должен: 
# Принимать расстояние distance в километрах.
# Вычислять время в пути в часах, основываясь на средней скорости для каждого типа транспортного средства (время = расстояние / скорость):
# для автомобиля средняя скорость — 60 км/ч;
# для велосипеда средняя скорость — 15 км/ч.
# Задача — реализовать методы calculate_travel_time() для каждого класса. 
# Вызвать метод calculate_travel_time() для каждого экземпляра, передав в качестве параметра расстояние: 120 для car и 45 для bicycle.


class Car:
    def calculate_travel_time(self, distance):
        return distance / 60


class Bicycle:
    def calculate_travel_time(self, distance):
        return distance / 15

car = Car()
bicycle = Bicycle()


# вызови метод calculate_travel_time() для каждого экземпляра, 
# передав в качестве параметра расстояние

print(car.calculate_travel_time(120))
print(bicycle.calculate_travel_time(45))


