import PySimpleGUI as sg
from abc import ABC, abstractmethod
import sys
class BankService(ABC):
    def __init__(self, amount: float, rate: float):
        self._amount = None
        self._rate = None
        self.amount = amount  # Используем сеттер
        self.rate = rate      
    @abstractmethod
    def calculate(self):
        pass
    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self, value):
        if value <= 0:
            raise ValueError("Сумма должна быть больше 0.")
        self._amount = value
    @property
    def rate(self):
        return self._rate
    @rate.setter
    def rate(self, value):
        if not 0 < value <= 100:
            raise ValueError("Процентная ставка должна быть в диапазоне (0, 100].")
        self._rate = value
class Loan(BankService):#Класс для кредита
    def __init__(self, amount, rate, term):
        super().__init__(amount, rate)
        self.term = term  # срок кредита в годах
    @property
    def term(self):
        return self._term
    @term.setter
    def term(self, value):
        if value <= 0:
            raise ValueError("Срок должен быть больше 0.")
        self._term = value
    def calculate(self):
        monthly_rate = self.rate / 12 / 100# Месячный платёж(аннуитетный)
        months = self.term * 12
        monthly_payment = self.amount * (monthly_rate * (1 + monthly_rate) ** months) / (
            (1 + monthly_rate) ** months - 1
        )
        return monthly_payment
    def __repr__(self):
        return f"<Loan: {self.amount} at {self.rate}% for {self.term} years>"
    def __eq__(self, other):
        return (
            isinstance(other, Loan)
            and self.amount == other.amount
            and self.rate == other.rate
            and self.term == other.term
        )
class Installment(BankService):
    def __init__(self, amount, rate):
        super().__init__(amount, rate)
    def calculate(self, months):
        return self.amount / months + self.amount * (self.rate / 12 / 100)# Платёж за месяц при рассрочке
    def __repr__(self):
        return f"<Installment: {self.amount} at {self.rate}%>"
    def __eq__(self, other):
        return isinstance(other, Installment) and self.amount == other.amount and self.rate == other.rate
class Deposit(BankService):
    def __init__(self, amount, rate, term):
        super().__init__(amount, rate)
        self.term = term  # срок вклада в годах
    @property
    def term(self):
        return self._term
    @term.setter
    def term(self, value):
        if value <= 0:
            raise ValueError("Срок должен быть больше 0.")
        self._term = value
    def calculate(self):
        return self.amount * (1 + self.rate / 100) ** self.term # Сумма вклада после начисления процентов
    def __repr__(self):
        return f"<Deposit: {self.amount} at {self.rate}% for {self.term} years>"
    def __eq__(self, other):
        return (
            isinstance(other, Deposit)
            and self.amount == other.amount
            and self.rate == other.rate
            and self.term == other.term
        )
def main():#Интерфейс пользователя
    import PySimpleGUI as sg
    layout = [
    [
        sg.Text("Выбор услуги:", size=(15, 1)),
        sg.Combo(["Кредит", "Рассрочка", "Вклад"], key="service")
    ],
    [sg.Text("Сумма:", size=(15, 1)), sg.Input(key="amount")],
    [sg.Text("Процентная ставка:", size=(15, 1)), sg.Input(key="rate")],
    [sg.Text("Срок (лет):", size=(15, 1)), sg.Input(key="term")],
    [sg.Button("Рассчитать"), sg.Button("Выход")],
    [sg.Output(size=(50, 10))],
]

    window = sg.Window("Банковские услуги", layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Выход"):
            break

        
        if event == "Рассчитать":
            print("Расчет услуги...")
    window.close()

if __name__ == "__main__":
    main()