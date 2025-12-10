# Создай класс Movies:
# проинициализируй в нём пустой список self.movies через конструктор;
# добавь метод add_movie(). Он будет принимать параметр movie и добавлять его в конец списка self.movies.
# Создай два дочерних класса — Comedy и Drama. Они наследуют метод add_movie(). 
# Метод этих классов должен принимать параметр movie и добавлять его в конец списка self.movies. 
# Затем возвращать записи вида Комедии: '[]' и Драмы: '[]' соответственно.
# Вызови метод add_movie() для объекта Comedy(). Входной параметр — 'Большой куш'. Выведи на экран результат.
# Вызови метод add_movie() для объекта Drama(). Входной параметр — 'Оружейный барон'. Выведи на экран результат.


class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
        return self.movies  # возвращаем список фильмов

    
class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return (f'Комедии: {self.movies}')
    

class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return (f'Драмы: {self.movies}')


comedy = Comedy()
comedy = comedy.add_movie('Большой куш')
print(comedy) 