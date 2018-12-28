---
layout: default
title: Expressions & Statements
grand_parent: Reference
parent: Week 2
nav_order: 4
permalink: /week-02/expressions-statements
---


# Expressions & Statements

## Operators
Operators are special symbols in Python that carry out arithmetic or logical computation. The value that the operator operates on is called the operand (e.g. a, b, and c below). Operators do different things depending on the **data type** of the operand. For example:

```python
>>> 3 + 2
6
>>> '3' + '2'
'32'
```

### Arithmetic Operators
```python
a = 10
b = 20
c = 25
```

| + | Addition | Adds values on either side of the operator | a + b = 30 |
| - | Subtraction | Subtracts right hand operand from left hand operand | a – b = -10 |
| * | Multiplication |	Multiplies values on either side of the operator | a * b = 200 |
| / | Division | Divides left hand operand by right hand operand	| b / a = 2 |
| % | Modulus | Divides left hand operand by right hand operand and returns remainder |	c % a = 5 |
| ** | Exponent | Performs exponential (power) calculation on operators	| a**b = 10 to the power 20 |
| // | Floor Division | The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity) | c // a = 2 |

Here is an example of some of the arithmetic operators in action (using numeric values):
<iframe width="100%" height="450" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=a%20%3D%2010%0Ab%20%3D%2020%0Ac%20%3D%2025%0Aresult%20%3D%20a%20%2B%20b%20%20%23%20addition%0Aresult%20%3D%20a%20-%20b%20%20%23%20subtraction%0Aresult%20%3D%20a%20*%20b%20%20%23%20multiplication%0Aresult%20%3D%20a%20/%20b%20%20%23%20division%0Aresult%20%3D%20c%20%25%20a%20%20%23%20remainer%0Aresult%20%3D%20c%20//%20a%20%23%20quotient%0A&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


### Comparison Operators
Comparison operators compare two operands according to a comparison rule and evaluate to either True or False (boolean). They are useful for branching logic: if some condition is True, then do something. Otherwise, do something else.

```python
a = 10
b = 20
```

| == | If the values of two operands are equal, then the condition becomes true. |	(a == b) is false. |
| != | If values of two operands are not equal, then condition becomes true. | (a != b) is true. |
| <> | If values of two operands are not equal, then condition becomes true. | (a <> b) is true. This is similar to != operator. |
| > | If the value of left operand is greater than the value of right operand, then condition becomes true. | (a > b) is false. |
| < | If the value of left operand is less than the value of right operand, then condition becomes true. | (a < b) is true. |
| >= | If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. | (a >= b) is false. |
| <= | If the value of left operand is less than or equal to the value of right operand, then condition becomes true. | (a <= b) is true. |

Here is an example of some of the comparison operators in action (using numeric values):
<iframe width="100%" height="450" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=a%20%3D%2010%0Ab%20%3D%2020%0Ac%20%3D%2010%0Aresult%20%3D%20a%20%3D%3D%20b%0Aresult%20%3D%20a%20%3D%3D%20c%0Aresult%20%3D%20a%20!%3D%20b%0Aresult%20%3D%20a%20%3E%20b%0Aresult%20%3D%20a%20%3C%20b%0Aresult%20%3D%20a%20%3E%3D%20b%0Aresult%20%3D%20a%20%3C%3D%20b&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

### Assignment Operators
Assignment operators are a way of saying: "put the results of the expression stored in the right operand into the left operand." 

| =	| Assigns values from right side operands to left side operand | c = a + b assigns the value of a + b into c |
| += | It adds right operand to the left operand and assign the result to left operand	| c += a is equivalent to <br>c = c + a |
| -= | It subtracts right operand from the left operand and assign the result to left operand	| c -= a is equivalent to <br>c = c - a |
| *= | It multiplies right operand with the left operand and assign the result to left operand | c *= a is equivalent to <br>c = c * a |
| /= | It divides left operand with the right operand and assign the result to left operand | c /= a is equivalent to <br>c = c / a |

Here is an example of some of the assignment operators in action (using numeric values):
<iframe width="100%" height="350" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=a%20%3D%2020%0Ab%20%3D%2040%0Ac%20%3D%20a%0Ac%20%2B%3D%20b%0Ac%20-%3D%20b%0Ac%20*%3D%20b%0Ac%20/%3D%20b&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


## Built-In Functions
Python has a number of built-in functions. A few of them are listed below. For the complete list, please check out the [Python reference](https://docs.python.org/3/library/functions.html).

### dir
Tells you a list of valid attributes for the object or type you pass in as an argument. Very useful for learning the different kinds of data or build-in functions are associated with the object:
```python 
>>> dir('hello')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(3)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

### type
Tells you what kind of data you have:
```python 
>>> type(10)
<class 'int'>
>>> type(2.5)
<class 'float'>
>>> type('Hello world!')
<class 'str'>
>>> type([1, 2, 3, 4, 5])
<class 'list'>
>>> type({'juniors': 40, 'freshmen': 34})
<class 'dict'>
```

### print
Prints a string or list of strings to the console
```python 
>>> print('Hello world!')
Hello world!
```

### len
The length of an operator
```python 
>>> len('Hello world!')
12
>>> len([1, 2, 3, 4, 5, 77, 33, 22])
8
```

### str
Converts a non-string to a string
```python 
>>> str(123)
'123'
```

### int
Converts a piece of data to an integer (if it can):
```python 
>>> int('123')
123
>>> int('www')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'www'
```