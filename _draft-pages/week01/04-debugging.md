---
layout: default
title: Debugging
grand_parent: Reference
parent: Week 1
nav_order: 3
permalink: /week-01/debugging
---

# Debugging
{: .no_toc }

1. TOC
{:toc}

## Managing the rigidity of computing [1]
Python is waiting for your command. You are encouraged to experiment with the language, even though you may not yet know its full vocabulary and structure. However, be prepared for errors. While computers are tremendously fast and flexible, they are also extremely rigid. The nature of computers is described in Stanford's introductory course as follows:


> **computer = powerful + stupid**
> 
> Computers are very powerful, looking at volumes of data very quickly. Computers can perform billions of operations per second, where each operation is pretty simple.
> 
> Computers are also shockingly stupid and fragile. The operations that they can do are extremely rigid, simple, and mechanical. The computer lacks anything like real insight ... it's nothing like the HAL 9000 from the movies. If nothing else, you should not be intimidated by the computer as if it's some sort of brain. It's very mechanical underneath it all.
> 
> Programming is about a person using their real insight to build something useful, constructed out of these teeny, simple little operations that the computer can do.
> 
> — Francisco Cai and Nick Parlante, Stanford CS101
{: .quote}

The rigidity of computers will immediately become apparent as you experiment with the Python interpreter: even the smallest spelling and formatting changes will cause unexpected output and errors. Learning to interpret errors and diagnose the cause of unexpected errors is called debugging. Some guiding principles of debugging are:

1. **Test incrementally:** Every well-written program is composed of small, modular components that can be tested individually. Try out everything you write as soon as possible to identify problems early and gain confidence in your components.
2. **Read the error messages:** Read the error messages carefully -- they will help you identify bugs, and understand why the program is not working.
3. **Isolate errors:** An error in the output of a statement can typically be attributed to a particular modular component. When trying to diagnose a problem, trace the error to the smallest fragment of code you can before trying to correct it.
4. **Check your assumptions:** Interpreters do carry out your instructions to the letter — no more and no less. Their output is unexpected when the behavior of some code does not match what the programmer believes (or assumes) that behavior to be. Know your assumptions, then focus your debugging effort on verifying that your assumptions actually hold.
5. **Consult others:** You are not alone! If you don't understand an error message, ask a friend, instructor, or search engine. If you have isolated an error, but can't figure out how to correct it ask someone else to take a look. A lot of valuable programming knowledge is shared in the process of group problem solving.

## Types of Errors
There are three basic types of errors. While your Python linter can help you with syntax errors, runtime and logic errors can be considerably more difficult to debug. An example of each kind of error is shown below:

### Syntax errors
You forget the single quote at the end of 'Hello world!'
```python
>>> print('Hello world!)
  File "<stdin>", line 1
    print('Hello world!)
                       ^
SyntaxError: EOL while scanning string literal
```
### Runtime errors
Example 1: You were expecting your user to type in a *number*, but instead they typed in the word 'fifty.' Often, runtime errors happen when your program did not encounter data that it expected (e.g. Who types the word 'fifty' as opposed to the number 50?!!!?!!).

```python
>>> age = input('How old are you? ')
How old are you? Fifty
>>> num_age = int(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'fifty'
```

Example 2: When the interpreter tries to *run* the print statement, it sees that the values stored in the ***rate*** and ***time*** variables are ints. However, Python does not allow ints and strings to be concatenated. An explicit type cast is needed. The programmer made a perfectly resonable assumption about how the language ought to work, but the Python interpreter has responded by telling you that you can't do that!

```python
>>> rate = 60  # 60 miles per hour
>>> time = 3   # 3 hours
>>> print('You have traveled ' + rate * time + ' miles.')  # display distance traveled
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

### Logic errors
You are trying to print out the distance traveled, but accidentally calculate distance as (rate x rate) instead of as (rate x time):
```python
>>> rate = 60  # 60 miles per hour
>>> time = 3   # 3 hours
>>> print('You have traveled ' + str(rate * rate) + ' miles.')  # display distance traveled
You have traveled 3600 miles.
```

## Using the Visual Studio Code Python debugger

## Writing testable code

## References
[1] As printed in [Composing Programs, Section 1.1.5](http://composingprograms.com/pages/11-getting-started.html#errors)