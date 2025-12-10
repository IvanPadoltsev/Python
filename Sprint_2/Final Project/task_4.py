# С помощью переменной hourly_payment установи почасовой уровень оплаты, равный 400.
# Проинициализируй атрибуты name, hours, rest_days, email через конструктор.
# Добавь метод класса get_hours(). Если значение hours неизвестно, метод рассчитывает часы, исходя из количества выходных — rest_days. 
# Формула для этого случая такая: (7 - rest_days) * 8.
# Добавь метод класса get_email(). Если значение email неизвестно, метод генерирует его так: f"{name}@email.com".
# Добавь метод класса set_hourly_payment(). Он меняет значение переменной hourly_payment.
# Добавь метод расчёта заработной платы salary(). Формула расчёта такая: hours * hourly_payment.


class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours = None, rest_days = None, email = None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours=None, rest_days=None, email=None):
        if hours is not None:
            return cls(name, hours, rest_days, email)
        elif rest_days is not None:
            calculated_hours = (7 - rest_days) * 8
            return cls(name, calculated_hours, rest_days, email)
        else:
            return cls(name, hours, rest_days, email)


    @classmethod
    def get_email(cls, name, hours=None, rest_days=None, email=None):
        if email is not None:
            return cls(name, hours, rest_days, email)
        else:
            generated_email = f"{name}@email.com"
            return cls(name, hours, rest_days, generated_email)
        
    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment


    def salary(self):
        if self.hours is None:
            return None
        
        salary_amount = self.hours * self.hourly_payment
        return salary_amount
    


emp1 = EmployeeSalary.get_hours("Алексей", rest_days=2, email="alex@company.com")
print(f"Имя: {emp1.name}")
print(f"Email: {emp1.email}")
print(f"Часы: {emp1.hours}")  # (7 - 2) * 8 = 40
print(f"Зарплата: {emp1.salary()}")  # 40 * 400 = 16000

# Использование класс-метода get_email для создания экземпляра
emp2 = EmployeeSalary.get_email("Ольга", hours=160)
print(f"\nИмя: {emp2.name}")
print(f"Email: {emp2.email}")  # Сгенерируется: Ольга@email.com
print(f"Часы: {emp2.hours}")
print(f"Зарплата: {emp2.salary()}")  # 160 * 400 = 64000

# Изменение почасовой оплаты через класс-метод
EmployeeSalary.set_hourly_payment(450)

# Проверяем изменение зарплаты
print(f"\nЗарплата Алексея после повышения: {emp1.salary()}")  # 40 * 450 = 18000
print(f"Зарплата Ольги после повышения: {emp2.salary()}")     # 160 * 450 = 72000

# Обычный способ создания экземпляра тоже работает
emp3 = EmployeeSalary("Петр", hours=120, email="petr@company.com")
print(f"\nИмя: {emp3.name}")
print(f"Зарплата Петра: {emp3.salary()}")  # 120 * 450 = 54000