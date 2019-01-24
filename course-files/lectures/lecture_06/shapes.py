def make_circle(canvas, center, radius, color='#FF4136'):
    x, y = center
    return canvas.create_oval(
        [ x - radius, y - radius, x + radius, y + radius ],
        fill=color,
        width=1
    )

def make_rectangle(canvas, top_left, width, height, color="#3D9970"):
    x, y = top_left
    print(x, y, x, y, x + width, x + height)
    return canvas.create_rectangle(
        x, y, x + width, x + height, 
        fill=color, 
        width=0
    )

def get_coordinates(canvas, id):
    return canvas.coords(id)

def set_coordinates(canvas, id, coordinates):
    canvas.coords(id, coordinates)

def move(canvas, id, x, y):
    coords = get_coordinates(canvas, id)
    print(coords)
    # update coordinates:
    for i in range(0, len(coords)):
        if i % 2 == 0:
            coords[i] += x
        else:
            coords[i] += y

    # set the coordinates:
    set_coordinates(canvas, id, coords)