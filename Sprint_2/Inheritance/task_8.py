# Есть суперкласс Artist, который описывает художника. У этого класса есть метод create_art(). 
# Он принимает один аргумент — время, которое художник потратит на создание произведения искусства. По умолчанию это 5 часов. 
# Метод create_art() возвращает количество произведений искусства, которые художник может создать за указанное время.
# Подкласс Sculptor наследуется от Artist. Тебе нужно переопределить в нём метод create_art() так, чтобы он принимал количество камня — stone, а не времени — time. 
# Метод create_art() должен возвращать количество скульптур, которые скульптор может создать из заданного количества камня.


class Artist:
    def __init__(self):
        self.art_creation_time = 5  # часов на одну картину

    def create_art(self, time):
        return time // self.art_creation_time


class Sculptor(Artist):
    def __init__(self):
        super().__init__()
        self.stone_needed = 3  # камня на одну скульптуру

    # переопредели метод create_art()
    def create_art(self, stone):
        return stone // self.stone_needed


painter = Artist()
print(painter.create_art(20))    # 4 картины

sculptor = Sculptor()
print(sculptor.create_art(8))    # 2 скульптуры