def _print_title(title):
    print('\n')
    print('#' * len(title))
    print(title)
    print('#' * len(title))

def problem_1a():
    # infinite loop:
    _print_title('Problem 1.a.')
    print('infinite loop!')
    return
    # i = 0
    # while i < 3:
    #     if i % 2 == 0:
    #         continue
    #     print(i = 0)
    #     i += 1

def problem_1b():
    _print_title('Problem 1.b.')
    notes = [27, 44, 30, 26, 17, 28, 46]
    for note in notes:
        if note // 3 == 9:
            print(note)

def problem_1c():
    _print_title('Problem 1.c.')
    j = 5
    m = 3
    k = j / m
    if k == 1:
        print('one')
    elif k == 2:
        print('two')
    elif k == 3:
        print('three')
    else:
        print('default')


def problem_2a():
    _print_title('Problem 2.a.')

    def area_of_square(length):
        return length * length
    
    def volume_of_cube(area):
        area * 6

    print(
        'Volume of a cube where side=10 feet is:', 
        volume_of_cube(area_of_square(10)), 
        'feet'
    )

def problem_2b():
    _print_title('Problem 2.b.')

    def make_mad_lib(exclamation, adverb, noun, adjective):
        print(
            exclamation + '! he said adverb as he jumped into his convertible ' + noun + ' and drove off with his ' + adjective + ' wife.'
        )
    make_mad_lib('Move it', 'angrily', 'Mazda Miata', 'annoyed')
        

def problem_2c():
    _print_title('Problem 2.c.')

    
nums = [9, 25, 16, 4, 81, 100, 64, 49, 36]
new_list = []
def sqrt(n):
    return int(n ** 0.5)

i = 0
while i < len(nums):
    if i % 3 == 0:
        new_list.append(sqrt(nums[i]))
    else:
        new_list.append(nums[i])
    i += 1

print(new_list)



def problem_3():
    _print_title('Problem 3')
    values = [5, 2, 5, 0, -2, -4, -7, 4, 7, 8]
    i = 0					
    while i < 10:
        num_neg = 0
        num_zero = 0				
        num_pos = 0
        if values[i] < 0:
            num_neg += 1
        elif values[i] == 0:
            num_zero += 1
        else:	
            num_pos += 1
        break			
                
    print('num_neg is:',  num_neg)
    print('num_zero is:',  num_zero)
    print('num_pos is:',  num_pos)


def problem_4():
    _print_title('Problem 4')
    def pennies_count(num_pennies):
        return [
            num_pennies // 100,
            num_pennies % 100
        ]

    result = pennies_count(234)
    print('pennies:', 234)
    print('dollars:', result[0])
    print('cents:', result[1])

def problem_5():
    _print_title('Problem 5')

    def add_it_up(numbers):
        sum = 0
        for n in numbers:
            sum += n
        return sum
    
    scores = [4.5, 2.5, 0.5, 9.0, 20.0]			
    sum_of_values = add_it_up(scores)			
    print('The sum of values in the list is:',  sum_of_values)

def problem_6():
    _print_title('Problem 6')

    def print_greeting(text, symbol='*'):
        print(symbol * (len(text) + 4))
        print(symbol, text, symbol)
        print(symbol * (len(text) + 4))
    
    print_greeting('Hello! How are you doing?')
    print_greeting('Practice Exam 1', symbol='#')


problem_1a()
problem_1b()
problem_1c()
problem_2a()
problem_2b()
problem_2c()
problem_3()
problem_4()
problem_5()
problem_6()