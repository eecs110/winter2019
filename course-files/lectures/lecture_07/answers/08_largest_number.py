# Challenge: write a program, using a for loop, to calculate the 
# largest number in the list:
numbers = [65, 1800, 12, 20, 1963, 5000, 260, 0, 40, 953, 775, 67, 33]
biggest_number_yet = 0
for num in numbers:
	if biggest_number_yet < num:
	      biggest_number_yet = num

print('The biggest number in the list is: ', biggest_number_yet)