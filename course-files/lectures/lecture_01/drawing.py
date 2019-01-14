from turtle import Turtle, Screen

turtle = Turtle()
# turtle.speed(speed=0)   # no animation
# turtle.hideturtle()     # hide turtle
turtle.color('red')
counter = 0
times = 7 * 5  # 7 rotations, 5 points

while True:
    turtle.forward(100)
    turtle.left(70)
    if counter == times:
        break
    counter += 1

screen = Screen()
screen.exitonclick()