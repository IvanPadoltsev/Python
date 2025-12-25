# Класс Employee хранит данные о сотрудниках. Напиши геттер и сеттер для приватного атрибута __salary.
# Добавь в сеттер условие: если зарплата меньше нуля, программа должна напечатать "Зарплата не может быть отрицательной".


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    # напиши здесь геттер для __salary
    @property
    def salary(self):
        return print(f'Зпшка: {self.__salary}')

    # напиши здесь сеттер для __salary
    def set_salary(self, salary):
        if salary < 0:
            print("Зарплата не может быть отрицательной")
        else:
            self.__salary = salary


emp = Employee('Вася', 100)
emp.salary
emp.set_salary(200)
emp.salary