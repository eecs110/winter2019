---
layout: default
parent: Reference
title: Statements
nav_order: 2
permalink: data-types
---

# Variables, Expressions and Statements
{: .no_toc }

1. TOC
{:toc}

## Values and Data Types

### Numbers
int: Integers
float: Decimals

### Strings

### Lists

### Dictionaries

## Variables
Variables are **temporary containers** that can hold data, functions, classes, and objects (i.e. anything you want). They are useful for temporary storage. You can stash information inside of variables, and then manipulate that information as needed. Think of variables as buckets that you can put things into and take things out of. For example, consider the following Pyagram:
<iframe width="100%" height="350" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=fname%20%3D%20'Lester'%0Alname%20%3D%20'Jones'%0Amsg%20%3D%20'Hi,%20'%20%2B%20fname%20%2B%20'%20'%20%2B%20lname%0Aprint%28msg%29%0Afname%20%3D%20'Tina'%0Amsg%20%3D%20'Hi,%20'%20%2B%20fname%20%2B%20'%20'%20%2B%20lname%0Aprint%28msg%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

In the code sample above, the variable `fname` and the variable `msg` are reused. Both are used as temporary storage as the program works to print two lines to the console (which is the only thing the user actually sees).

### Naming variables

### Reserved words
The following words mean something special in Python. Therefore, you cannot name your variable any of these words.

```
and         del         global      not       with
as          elif        if          or        yield
assert      else        import      pass
break       except      in          raise
class       finally     is          return
continue    for         lambda      try
def         from        nonlocal    while    
```

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
[List of built-in functions](https://www.w3schools.com/python/python_ref_functions.asp)
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


## Modules
Something about modules.
