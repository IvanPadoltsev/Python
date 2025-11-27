# В словаре types хранятся типы багов. Его ключи — числа от 1 до 5, а значения — от 'Блокирующий'  до 'Тривиальный' соответственно. 

# В словаре tickets хранятся тикеты (задачи), которые заведены на эти баги. 
# Ключи — числовое значение критичности от 1 до 5, а значения — список с тикетами, которые этим значениям критичности соответствуют. 
# Но некоторые тикеты добавлены несколько раз в разные списки.

# Составь итоговый словарь, где ключи — это значение критичности, например, 'Значительный', а значения — списки с уникальными тикетами. 
# Для этого напиши две функции: 
# одна удаляет дубли из списков с тикетами,
# вторая связывает уровень критичности со списком уникальных тикетов.
# Если тикет есть в одном списке, то он уже не может быть в списках на уровень ниже. 
# Вторая функция принимает на вход два параметра: словарь types с типами багов и словарь tickets со списком багов. Функция возвращает словарь, где уровень критичности связан со списком уникальных тикетов.
# Итоговый словарь должен получиться таким:
# tickets_by_type = {
#     'Блокирующий': ['API_45', 'API_76', 'E2E_4'],
#     'Критический': ['UI_19', 'API_65', 'E2E_45'],
#     'Значительный': ['E2E_2'],
#     'Незначительный': ['E2E_9'],
#     'Тривиальный': ['API_61']
# }
# Вызывать функцию необязательно.


types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}


# Удаляет дубли из списков с тикетами
def remove_duplicates(tickets_dict): 
    cleaned_tickets = {}
    all_used_tickets = []  # список всех использованных тикетов
   
    for level in range(len(tickets_dict) + 1):
        #print(level)
        if level in tickets_dict:
            current_level_tickets = []

            for ticket in tickets_dict[level]: # Если тикет еще не встречался, добавляем его
                if ticket not in all_used_tickets:
                    current_level_tickets.append(ticket)
                    all_used_tickets.append(ticket)
                    #print(current_level_tickets) 
            cleaned_tickets[level] = current_level_tickets

    
    return cleaned_tickets

# Связывает уровень критичности со списком уникальных тикетов
def link_tickets_to_types(types_dict, tickets_dict): 
    cleaned_tickets = remove_duplicates(tickets_dict)
    result = {}
    
    for level, ticket_list in cleaned_tickets.items():
        result[types_dict[level]] = ticket_list
    
    return result

# Получаем итоговый словарь
tickets_by_type = link_tickets_to_types(types, tickets)
print(tickets_by_type)