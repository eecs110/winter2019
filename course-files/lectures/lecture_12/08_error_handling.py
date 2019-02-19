# This loop keeps going until the user has entered a valid age:
while True:
    age = input('how old are you? ')
    try:
        age = int(age)
        print('Your age is:', age)
        break
    except:
        # Note: this code uses the string "format" method.
        print('Invalid age: "{age}". Please enter an integer.'.format(age=age))