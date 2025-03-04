def calculate_deposit(principal: float, annual_rate: float, months: int): #Расчет суммы вклада (сложные проценты)
    monthly_rate = annual_rate / 12 / 100
    final_amount = principal * (1 + monthly_rate) ** months
    return round(final_amount, 2)