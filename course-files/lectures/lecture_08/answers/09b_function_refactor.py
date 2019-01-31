# Perhaps an even simpler way to do string substitution:
# https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat
import os

def generate_email(name, amount, level, gift, outfile=None):
    banner = '-' * 98
    
    print(f'''
    {banner}
    Dear {name},

    Thank you for donating ${amount:,} to the Southern Poverty Law Center. We really appreciate donors like
    you. Because of your support, you are eligible to become a {level}-level supporter. As a token of
    our appreciation, please accept this {gift}.

    We look forward to your continued sponsorship.

    Sincerely,

    SPLC
    {banner}
    

    ''', file=outfile)

def get_file(name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = os.path.join(dir_path, name)
    return open(file_name, "a")

f = get_file('emails.txt')

generate_email('Meredith', 50, 'bronze', 'coffee mug', outfile=f)
generate_email('Toby', 150, 'silver', 'engraved pen', outfile=f)
generate_email('Tomar', 250, 'gold', 'T-Shirt', outfile=f)
generate_email('Natasha', 1250, 'platinum', 'gold pendant', outfile=f)