'''
NOTE: This code requires a third party module called pyfiglet.
NOTE: This example is a visual representation, and will not be useful
for people who are blind / have limited vision.
You will need to install this module from the command line before
this code can run. To do it, open up the Terminal (Mac) or Anaconda
Command Prompt (Windows) and type the following command (from any directory):

$ pip install pyfiglet

'''

# imports a module
from pyfiglet import figlet_format
import os

def print_fancy_greeting(name, file_destination):
    # available fonts: http://www.figlet.org/examples.html
    # starwars, contessa, cosmic, cyberlarge
    greeting = 'Hello, ' + name + '!'
    ascii_representation = figlet_format(greeting, font='contessa')
    print(ascii_representation)
    print(ascii_representation, file=file_destination)

# create a file:
dir_path = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(dir_path,"demofile.txt")
demofile = open(file_name, "a")

# ask someone for their first and last name:
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

# print a greeting:
print_fancy_greeting(first_name + ' ' + last_name, file_destination=demofile)