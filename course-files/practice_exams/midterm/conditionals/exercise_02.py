def calculate_gross_pay(hours, rate):
    if hours > 40:
        regular_pay = 40 * rate
        overtime = (hours - 40) * rate * 1.5
        return regular_pay + overtime
    else:
        return hours * rate


wage = int(input('What is your hourly wage? '))
hours = int(input('How many hours did you work this week? '))
print('Your gross pay is:', calculate_gross_pay(wage, hours))