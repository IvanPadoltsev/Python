# Сделай из функции func лямбда-функцию.
# Сохранять условную конструкцию не нужно: лямбда-функцию можно написать без неё.


def func(x):
    if 10 > x > 0:
        return True
    else: 
        return False

# перепиши функцию func в виде лямбда-функции

lambda x: 10 > x > 0


print((lambda x: 10 > x > 0)(-1)) # False
print((lambda x: 10 > x > 0)(0)) # False
print((lambda x: 10 > x > 0)(1)) # True
print((lambda x: 10 > x > 0)(5)) # True
print((lambda x: 10 > x > 0)(10)) # False
print((lambda x: 10 > x > 0)(11)) # False