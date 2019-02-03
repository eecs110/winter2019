def calculate_gross_pay(hours, rate):
    return hours * rate

wage = int(input('What is your hourly wage? '))
hours = int(input('How many hours did you work this week? '))
print('Your gross pay is:', calculate_gross_pay(wage, hours))