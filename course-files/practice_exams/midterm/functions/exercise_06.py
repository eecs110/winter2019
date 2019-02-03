## Example 6: global variables can be accessed from within functions 
## (though this is not recommended). Best practice is to pass in all the variables
## the function needs via parameters
name1 = 'Lindsay'

def scope_demo_2(name):
   print(name)
   print(name1)

scope_demo_2('Walter')

# Visualize it: https://goo.gl/kgrp1r