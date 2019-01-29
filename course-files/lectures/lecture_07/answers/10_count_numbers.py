# Challenge: write a program that counts all of the negative, positive, and zero
# values in the values list
numbers = [5, 2, 5, 0, -2, -4, -7, 4, 7, 8]
num_neg = 0
num_zero = 0				
num_pos = 0
    					
for num in numbers:
    if num < 0:
        num_neg += 1
    elif num == 0:
        num_zero += 1
    else:	
        num_pos += 1			
            
print('num_neg is:',  num_neg)
print('num_zero is:',  num_zero)
print('num_pos is:',  num_pos)