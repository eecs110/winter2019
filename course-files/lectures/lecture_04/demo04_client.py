# This code sample draws from the module called demo04_module.
# It is an example of a module that you can make for yourself!
import demo04_module
import os

side_a = int(input('What is the length of the first side? '))
side_b = int(input('What is the length of the second side? '))

hypotenuse = demo04_module.get_hypotenuse(side_a, side_b)
print('The hypotenuse is:', hypotenuse)

area = demo04_module.get_area(side_a, side_b)
print('The area is:', area)

perimeter = demo04_module.get_perimeter(side_a, side_b)
print('The perimeter is:', perimeter)

# write the dimensions to a file (which will be written)
dir_path = os.path.dirname(os.path.realpath(__file__))
file_name = os.path.join(dir_path,"dimensions.csv")
dimensions_file = open(file_name, "a")
demo04_module.write_to_file(side_a, side_b, dimensions_file)