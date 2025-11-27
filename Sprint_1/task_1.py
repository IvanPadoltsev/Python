# Строка содержит пять временных значений. Они записаны через запятую:
# '1h 45m,360s,25m,30m 120s,2h 60s'.
# Напиши цикл, который посчитает общее количество минут. Результат сохрани в переменную и выведи на экран. Используй в решении методы split(), replace() и оператор in.
# Обрати внимание: временное значение может состоять из одного, двух или трёх единиц времени. Значения расшифровываются так:
# часы — любое положительное целое число и символ h;
# минуты — любое положительное целое число и символ m;
# секунды — положительное целое число кратное 60 и символ s.


time = '1h 45m,360s,25m,30m 120s,2h 60s'

time_split = time.split(',')

time_total = 0

for values in time_split:
    time_stamps = values.split()

    total_minutes = 0

    for time_stamp in time_stamps:
        if 'h' in time_stamp:
            hours = int(time_stamp.replace('h', ''))
            total_minutes += hours * 60
        elif 'm' in time_stamp:
            minutes = int(time_stamp.replace('m', ''))
            total_minutes += minutes
        elif 's' in time_stamp:
            seconds = int(time_stamp.replace('s', ''))
            total_minutes += seconds // 60
    time_total += total_minutes


print('Суммарное количество минут:', time_total)