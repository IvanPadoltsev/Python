# Есть суперкласс BankAccount, который описывает банковский счёт. В классе реализован метод withdraw() — снятие денег со счёта.
# Что нужно сделать:
# Создай подкласс SavingsAccount. В нём нужно вызывать конструктор суперкласса с balance. 
# Дополнительно должна быть переменная interest_rate: это годовая процентная ставка по счёту, которая также задаётся в конструкторе.
# В классе SavingsAccount переопредели метод withdraw():
# Рассчитывается комиссия commission. Она равна amount, умноженному на процентную ставку.
# Комиссия списывается вместе с суммой снятия. Используется метод withdraw() суперкласса.


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

        return self.balance


# наследуй класс от BankAccount и переопредели метод withdraw
class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        self.balance = super().withdraw(amount)
        self.balance -= amount * self.interest_rate

        return self.balance



# пример использования
acc = BankAccount(1000)
print(acc.withdraw(100))          # вывод: 900

savings_acc = SavingsAccount(1000, 0.05)
print(savings_acc.withdraw(100))  # вывод: 895