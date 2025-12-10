# Есть два вида тест-кейсов: автоматизированный и обычный. 
# Автоматизированный тест-кейс будет отличаться от обычного значением признака: is_automated. 
# У обычных кейсов будет значение False, у автоматизированных — True.
# Допиши статические методы в каждом из классов. Они должны проверять, будет тест-кейс автоматизированным или обычным.


test_case_1 = {'name': 'Проверить клик на кнопку поиска',
               'steps': ['Открыть сайт',
                        'Найти кнопку с надписью "поиск"',
                        'Кликнуть на кнопку'],
              'e_result': 'Появились результаты поиска',
              'result': 'Появились результаты поиска',
              'is_automated': False}
test_case_2 = {'name': 'Проверить цвет кнопки поиска',
               'steps': ['Открыть сайт',
                        'Найти кнопку с надписью "поиск"',
                        'Открыть свойства кнопки'],
                        'e_result': 'Цвет соответствует заявленному',
                        'result': 'Цвет не соответствует заявленному',
               'is_automated': False}
test_case_3 = {'name': 'Проверить клик на кнопку входа',
               'steps': ['Открыть сайт',
                        'Найти кнопку с надписью "войти"',
                        'Кликнуть на кнопку'],
              'e_result': 'Произошёл вход',
              'result': 'Passed',
              'is_automated': True}



class TestCase:

    def __init__(self, name, steps, e_result, result):
        self.name = name
        self.steps = steps
        self.expected_result = e_result
        self.result = result

    def get_case_in_str(self):
        return f'{self.name}, {self.steps}, {self.result}'
		
    # допиши метод так, чтобы он был статическим и проверял, является ли 
    # тест-кейс обычным
    @staticmethod
    def is_ordinary_case(test_case):
        if not test_case.get('is_automated'):
            return True
        else:
            return False

class AutomatedTestCase:

    def __init__(self, name, steps, e_result, result):
        self.name = name
        self.steps = steps
        self.expected_result = e_result
        self.result = result
		
    def get_case_in_str(self):
        return f'{self.name}, {self.steps}, {self.result}'

    # допиши метод так, чтобы он был статическим и проверял, является ли 
    # тест-кейс автоматизированным
    @staticmethod
    def is_automated_case(test_case):
        if test_case.get('is_automated'):
            return True
        else:
            return False

test_report = {'automated': [],
              'ordinary': [] }

def add_case_to_list(test_case):
    # допиши тут аргумент, который необходимо передать методу
    if AutomatedTestCase.is_automated_case(test_case):
        # а тут — создание объекта автоматизированного кейса
        automated_case = AutomatedTestCase(test_case.get('name'), test_case.get('steps'), test_case.get('e-result'), test_case.get('result'))
        automated_case = automated_case.get_case_in_str()
        test_report['automated'].append(automated_case)
    if TestCase.is_ordinary_case(test_case):
        ordinary_case = TestCase(test_case.get('name'), test_case.get('steps'), test_case.get('e-result'), test_case.get('result'))
        ordinary_case = ordinary_case.get_case_in_str()
        test_report['ordinary'].append(ordinary_case)

add_case_to_list(test_case_1)
add_case_to_list(test_case_2)
add_case_to_list(test_case_3)

print(test_report)