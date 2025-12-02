# Представь, что разрабатываешь игру, в которой есть разные типы существ: люди, вампиры, оборотни. Вампиры умеют превращаться в летучих мышей, оборотни — в волков. 
# Люди, не обладая подобными способностями, тем не менее могут бежать. 
# Задача — создать миксины, которые будут обеспечивать эти функции.
# Создай миксин BatTransformableMixin. Он должен содержать метод transform_into_bat(), который будет возвращать строку "Превращение в летучую мышь".
# Создай миксин WolfTransformableMixin. Этот миксин должен содержать метод transform_into_wolf(), который будет возвращать строку "Превращение в волка".
# Создай миксин RunnableMixin. Этот миксин должен содержать метод run(), который будет возвращать строку "Беги, Форрест, беги!".
# Создай классы Human, Vampire и Werewolf. Класс Human должен использовать миксин RunnableMixin. 
# Класс Vampire должен использовать миксины BatTransformableMixin и RunnableMixin. Класс Werewolf должен использовать миксин WolfTransformableMixin.
# Посмотри, что напечатают методы, вызванные для объектов human, vampire и werewolf.


class BatTransformableMixin:
    def transform_into_bat(self):
        return f'Превращение в летучую мышь!'
    

class WolfTransformableMixin:
    def transform_into_wolf(self):
        return f'Превращение в волка!'


class RunnableMixin:
    def run(self):
        return f'Беги, Форрест, беги!!!'        


# наследуется от RunnableMixin
class Human(RunnableMixin):
    pass


# наследуется от BatTransformableMixin и RunnableMixin
class Vampire(BatTransformableMixin, RunnableMixin):
    pass


# наследуется от WolfTransformableMixin
class Werewolf(WolfTransformableMixin):
    pass


human = Human()
vampire = Vampire()
werewolf = Werewolf()

print(human.run())                      
print(vampire.run())                    
print(vampire.transform_into_bat())     
print(werewolf.transform_into_wolf())