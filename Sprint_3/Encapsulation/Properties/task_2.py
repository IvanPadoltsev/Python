# Класс EBook представляет электронную книгу. В нём два приватных атрибута: 
# __content — содержание книги;
# __current_page — текущая страница.
# Содержание книги — это список строк. Каждая строка представляет страницу книги. Например, ['Cтраница 1', 'Страница 2', 'Страница 3'].
# Текущая страница — это индекс элемента в списке __content.
# Геттеры для атрибутов уже написаны. Твоя задача — добавить сеттеры:
# Сеттер для content устанавливает __content новое значение — new_content;
# Сеттер для current_page устанавливает значение page_number для __current_page. Но перед этим его проверяет:
# если page_number меньше нуля, значение текущей страницы равно нулю;
# если page_number больше или равно len(self.__content), значение текущей страницы равно len(self.__content) - 1;
# в остальных случаях __current_page получает значение page_number.


class EBook:
    def __init__(self, content):
        self.__content = content
        self.__current_page = 0

    @property
    def content(self):
        return self.__content
    
    # ... создай сеттер для свойства content
    @content.setter
    def content(self, new_content):
        self.__content = new_content

    @property
    def current_page(self):
        return self.__current_page

    # ... создай сеттер для свойства current_page
    @current_page.setter
    def current_page(self, page_number):
        if page_number < 0:
            self.__current_page = 0
        elif page_number >= len(self.__content):
            self.__current_page = len(self.__content) - 1
        else:
            self.__current_page = page_number