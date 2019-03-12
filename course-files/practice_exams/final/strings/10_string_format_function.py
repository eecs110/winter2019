# Write a function called print_animal_slogan that takes the name of
# an animal (a string) as an argument and prints the following 
# slogan with the animal name. Below, I show how I would call your function and what it would 
# output to the screen.
def print_animal_slogan(animal):
    template = '''
        How much wood could a {creature} chuck 
        If a {creature} could chuck wood? 
        As much wood as a {creature} could chuck, 
        If a {creature} could chuck wood.
        '''
    print(template.format(creature=animal))

print_animal_slogan('rabbit')
print_animal_slogan('woodchuck')
print_animal_slogan('lion')