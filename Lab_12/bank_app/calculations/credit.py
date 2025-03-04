# calculations/credit.py

def calculate_credit(principal: float, annual_rate: float, months: int):
    monthly_rate = annual_rate / 12 / 100
    payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)
    schedule = []
    balance = principal

    for month in range(1, months + 1):
        interest = balance * monthly_rate
        principal_payment = payment - interest
        balance -= principal_payment
        schedule.append({
            "Month": month,
            "Payment": round(payment, 2),
            "Principal": round(principal_payment, 2),
            "Interest": round(interest, 2),
            "Balance": round(balance, 2)
        })
    
    return schedule, round(payment, 2)