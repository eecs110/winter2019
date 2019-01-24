def make_circle(canvas, center, radius, color='#FF4136', tags=''):
    x, y = center
    return canvas.create_oval(
        [ x - radius, y - radius, x + radius, y + radius ],
        fill=color,
        width=1,
        tags=tags
    )

def make_rectangle(canvas, top_left, width, height, color="#3D9970", tags=''):
    x, y = top_left
    return canvas.create_rectangle(
        [(x, y), (x + width, y + height)], 
        fill=color, 
        width=0,
        tags=tags
    )

def get_coordinates(canvas, id):
    return canvas.coords(id)

def set_coordinates(canvas, id, coordinates):
    canvas.coords(id, coordinates)

def move(canvas, tag, x=2, y=0):
    ids = canvas.find_withtag(tag)
    for id in ids:
        coords = get_coordinates(canvas, id)
        
        # update coordinates:
        for i in range(0, len(coords)):
            if i % 2 == 0:
                coords[i] += x
            else:
                coords[i] += y

        # set the coordinates:
        set_coordinates(canvas, id, coords)