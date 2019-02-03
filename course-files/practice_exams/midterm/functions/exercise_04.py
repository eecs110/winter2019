## Write a function called "calculate_area" that calculates the area of a rectangle that 
## is represented by a 4 ints: top, right, bottom, left. Assume that the origin (0, 0) is
## in the top, left-hand corner, and that the user always passes in positive integers.


# SOLUTION:
def calculate_area(top, right, bottom, left):
    return (bottom - top) * (right - left)

print(calculate_area(100, 300, 200, 0))
print(calculate_area(50, 600, 100, 520))