from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    # move forwards
    turtle.forward(10)

def move_backward():
    # move backwards
    turtle.backward(10)

def turn_left():
    # turn left
    turtle.left(10)

def turn_right():
    # turn right
    turtle.right(10)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "space")
screen.exitonclick()
