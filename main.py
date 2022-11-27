from turtle import Turtle ,Screen
tim = Turtle()
scr = Screen()

def fmove():
    tim.forward(100)
def bmove():
    tim.backward(100)
def clockwise():
    tim.right(20)
def anticlock():
    tim.left(20)
def clear():
    tim.clear()
    tim.penup()
    tim.goto(0,0)

scr.listen()
scr.onkey(key="w", fun = fmove)
scr.onkey(key="s", fun = bmove)
scr.onkey(key="a", fun = clockwise)
scr.onkey(key="d", fun = anticlock)
scr.onkey(key="c", fun = clear)
scr.exitonclick()