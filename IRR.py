def npv_f(rate, cashflows):
    total = 0.0
    for i, cashflow in enumerate(cashflow):
        total += cashflow / (1 +rate)**i
    return total
