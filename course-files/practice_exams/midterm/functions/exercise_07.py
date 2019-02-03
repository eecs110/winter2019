## Example 7: local variables that are defined within function blocks
## cannot be accessed outside of them.
## The print(greeting) expression throws an error because the variable greeting
## was defined inside of a function, and therefore is destroyed after
## the function block executes:

def scope_demo_3(name):
   greeting = 'Welcome, '
   print(greeting + name)

scope_demo_3('Jimmy')
# print(greeting)  # uncomment this to see the error

# Visualize it: https://goo.gl/H3Tx4f
