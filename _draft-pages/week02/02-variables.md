---
layout: default
title: Variables
grand_parent: Reference
parent: Week 2
nav_order: 2
permalink: /week-02/variables
---

# Variables
Variables have a variety of uses. For one, they allow you to assign names to numbers, functions, objects, and modules, thereby making them more intuitive and human-readable. 

Variables can also be thought of as **temporary containers** that can hold data, functions, classes, and objects (i.e. anything you want). They are useful for temporary storage. You can stash information inside of variables, and then manipulate that information as needed. Think of variables as buckets that you can put things into and take things out of. For example, consider the following Pyagram:
<iframe width="100%" height="350" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=fname%20%3D%20'Lester'%0Alname%20%3D%20'Jones'%0Amsg%20%3D%20'Hi,%20'%20%2B%20fname%20%2B%20'%20'%20%2B%20lname%0Aprint%28msg%29%0Afname%20%3D%20'Tina'%0Amsg%20%3D%20'Hi,%20'%20%2B%20fname%20%2B%20'%20'%20%2B%20lname%0Aprint%28msg%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

In the code sample above, the variable `fname` and the variable `msg` are reused. Both are used as temporary storage as the program works to print two lines to the console (which is the only thing the user actually sees).

## Naming variables

## Reserved words
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
