## Scope Question: local variable takes precedent over global variable
## What will print to the screen?  Walter or Lindsay?
## Why?

name = 'Lindsay'
def scope_demo_1(name):
   print(name)

scope_demo_1('Walter')