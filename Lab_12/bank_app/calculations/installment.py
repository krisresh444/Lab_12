def calculate_installment(principal: float, months: int): #Рассчет рассрочки (без процентов)
    payment = principal / months
    schedule = [
        {"Month": month, "Payment": round(payment, 2), "Balance": round(principal - month * payment, 2)}
        for month in range(1, months + 1)
    ]
    return schedule