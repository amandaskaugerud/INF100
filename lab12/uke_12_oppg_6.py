def weekly_pay(hourly_rate, hours):
    pay = 0
    if hourly_rate < 200:
        return "Minstelønnskravet er ikke oppfylt"
    elif hours > 60:
        return "En ansatt jobber mer enn 60 timer"
    elif hours <= 40:
        pay = hours * hourly_rate
    elif 40 < hours <= 60:
        pay = (40 * hourly_rate) + (hours-40)*(hourly_rate*1.5)
    return int(pay)
