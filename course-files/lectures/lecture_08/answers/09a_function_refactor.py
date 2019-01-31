def generate_email(name, amount, level, gift):
    print('''
    Dear ''' + name + ''',

    Thank you for donating $''' + str(amount) + ''' to the Southern Poverty Law Center. We really appreciate donors like
    you. Because of your support, you are eligible to become a ''' + level + '''-level supporter. As a token of
    our appreciation, please accept this ''' + gift + '''.

    We look forward to your continued sponsorship.

    Sincerely,

    SPLC
    ''')


generate_email('Meredith', 50, 'bronze', 'coffee mug')
generate_email('Toby,', 150, 'silver', 'engraved pen')
generate_email('Tomar', 250, 'gold', 'T-Shirt')
