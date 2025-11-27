# Создай суперкласс ElectronicDevice. У него должны быть:
# метод power_on(), который печатает "Устройство включено";
# метод power_off(), который печатает "Устройство выключено".
# Затем создай два подкласса — Television и Computer. Они оба наследуются от ElectronicDevice, но у каждого своя специфика:
# для Television добавь метод change_channel(), который печатает "Канал был изменен";
# для Computer добавь метод open_application(), который печатает "Приложение было открыто".


# создай суперкласс ElectronicDevice

class ElectronicDevice:

    def power_on(self):
        print('Устройство включено')

    def power_off(self):
        print('Устройство выключено')


# создай подкласс Television
class Television(ElectronicDevice):

    def change_channel(self):
        print('Канал был изменен')    


# создай подкласс Computer
class Computer(ElectronicDevice):

    def open_application(self):
        print('Приложение было открыто')


electronic_device = ElectronicDevice()
electronic_device.power_on()
electronic_device.power_off()


television = Television()
television.power_on()
television.change_channel()
television.power_off()

computer = Computer()
computer.power_on()
computer.open_application()
computer.power_off()
