# This code sample draws from the module called 02_module.
# It is an example of a module that you can make for yourself!
import d2_my_module

side_a = int(input('What is the length of the first side? '))
side_b = int(input('What is the length of the second side? '))

hypotenuse = d2_my_module.get_hypotenuse(side_a, side_b)

area = d2_my_module.get_area(side_a, side_b)
perimeter = d2_my_module.get_perimeter(side_a, side_b)


print('The hypotenuse is:', hypotenuse)
print('The area is:', area)
print('The perimeter is:', perimeter)

# write the dimensions to a file:
d2_my_module.write_to_file(side_a, side_b, file_name='dimensions.csv', print_header=True, mode='w')

# print some other values, just to see them write to the module:
# d2_my_module.write_to_file(3, 7, file_name='dimensions.csv')
# d2_my_module.write_to_file(33, 77, file_name='dimensions.csv')
# d2_my_module.write_to_file(13, 57, file_name='dimensions.csv')
# d2_my_module.write_to_file(92, 66, file_name='dimensions.csv')
# d2_my_module.write_to_file(1, 4, file_name='dimensions.csv')