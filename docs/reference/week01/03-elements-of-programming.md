---
layout: default
title: Programming
grand_parent: Reference
parent: Week 1
nav_order: 2
permalink: /week-01/programming
---

# Programming Overview
{: .no_toc }

1. TOC
{:toc}

## Parts of a computer
* [How the CPU Works](http://www.it4nextgen.com/what-is-a-cpu-central-processing-unit/)
* Interpreter v. Compiler
* Using the command line

## What is a programming language? [1]
A programming language is more than just a means for instructing a computer to perform tasks. The language also serves as a framework within which we organize our ideas about computational processes. Programs serve to communicate those ideas among the members of a programming community. Thus, programs must be written for people to read, and only incidentally for machines to execute.

When we describe a language, we should pay particular attention to the means that the language provides for combining simple ideas to form more complex ideas. Every powerful language has three such mechanisms:

1. primitive expressions and statements, which represent the simplest building blocks that the language provides,
2. means of combination, by which compound elements are built from simpler ones, and
3. means of abstraction, by which compound elements can be named and manipulated as units.

In programming, we deal with two kinds of elements: **functions** and **data.** (Soon we will discover that they are really not so distinct.) Informally, data is stuff that we want to manipulate, and functions describe the rules for manipulating the data. Thus, any powerful programming language should be able to describe primitive data and primitive functions, as well as have some methods for combining and abstracting both functions and data.

## Building blocks of programs [2]
To introduce Python, the section below will walk through an example of a number of different language features. Then, we will spend the rest of the course unpacking these ideas from the ground up. Much of this section has been directly ported from John DeNero's [ComposingPrograms.com](http://composingprograms.com). A Jupyter Notebook of this particular example (and a few additional features) is available [here](https://github.com/eecs110/winter2019-course-files/blob/master/notebooks/01.%20Introduction.ipynb).

Python has built-in support for a wide range of common programming activities, such as manipulating text, displaying graphics, and communicating over the Internet. The line of Python code:

```python
>>> from urllib.request import urlopen
```
is an import statement that loads functionality for accessing data on the Internet. In particular, it makes available a function called urlopen, which can access the content at a uniform resource locator (URL), a location of something on the Internet.

### Statements & Expressions
Python code consists of expressions and statements. Broadly, computer programs consist of instructions to either

1. Compute some value
2. Carry out some action

***Statements*** typically describe actions. When the Python interpreter executes a statement, it carries out the corresponding action. On the other hand, ***expressions*** typically describe computations that yield a value. When Python evaluates an expression, it computes the value of that expression. This chapter introduces several types of statements and expressions.

The assignment statement:

```python
>>> shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')
```
associates the name shakespeare with the value of the expression that follows =. That expression applies the urlopen function to a URL that contains the complete text of William Shakespeare's 37 plays, all in a single text document.

### Functions
Functions encapsulate logic that manipulates data. urlopen is a function. A web address is a piece of data, and the text of Shakespeare's plays is another. The process by which the former leads to the latter may be complex,but we can apply that process using only a simple expression because that complexity is tucked away within a function.

Another assignment statement:

```python
>>> words = set(shakespeare.read().decode().split())
```

associates the name words to the set of all unique words that appear in Shakespeare's plays, all 33,721 of them. The chain of commands to read, decode, and split, each operate on an intermediate computational entity: we read the data from the opened URL, then decode the data into text, and finally split the text into words. All of those words are placed in a set.

### Objects
A set is a type of object, one that supports set operations like computing intersections and membership. An object seamlessly bundles together data and the logic that manipulates that data, in a way that manages the complexity of both.

### Interpreters
Evaluating compound expressions requires a precise procedure that interprets code in a predictable way. A program that implements such a procedure, evaluating compound expressions, is called an interpreter. 

When compared with other computer programs, interpreters for programming languages are unique in their generality. Python was not designed with Shakespeare in mind. However, its great flexibility allowed us to process a large amount of text with only a few statements and expressions.

## References
[1] As printed in [Composing Programs 1.2](http://composingprograms.com/pages/12-elements-of-programming.html)

[2] As printed in [Composing Programs 1.1.4](http://composingprograms.com/pages/11-getting-started.html#first-example)