# Класс Student хранит имя студента и его оценки. 
# Сделай так, чтобы значения grades можно было добавить только через метод add_grade. При этом атрибут можно наследовать.
# Добавь геттер, который вернёт список оценок.


class Student:
    def __init__(self, name):
        self.name = name
        self.__grades = []

    def add_grade(self, grade):
        if 1 <= grade <= 5:
            self.__grades.append(grade)
        else:
            print("Оценка должна быть между 1 и 5")

	# добавь геттер
    def get_grades(self):
        return self.__grades


student = Student('Двоечкин')
student.add_grade(2)
student.add_grade(2)
student.add_grade(2)
print(student.get_grades())