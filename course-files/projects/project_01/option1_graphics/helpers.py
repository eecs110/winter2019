import utilities

def make_creature(canvas, center, size=100, tag='creature', fill='hotpink'):
    # just a demo of how you might think about making your creature:
    left_eye_pos = (center[0] - size / 4, center[1] - size / 5)
    right_eye_pos = (center[0] + size / 4, center[1] - size / 5)
    eye_width = eye_height = size / 10
    utilities.make_circle(canvas, center, size, color=fill, tag=tag)
    utilities.make_oval(canvas, left_eye_pos, eye_width, eye_height, color='black', tag=tag)
    utilities.make_oval(canvas, right_eye_pos, eye_width ,eye_height, color='black', tag=tag)
    utilities.make_line(canvas, [
        (center[0] - size / 2, center[1] + size / 3), 
        (center[0], center[1] + size / 1.2), 
        (center[0] + size / 2, center[1] + size / 3)
    ], curvy=True)
    

def make_landscape_object(canvas, position, size=100):
    # your code to create your creature goes here:
    # replace the code below...
    print('make_landscape_object...')
    print('size:', size, 'center:', position) 