from turtle import Turtle , Screen
import random
t = Turtle()
scr = Screen()
scr.colormode(255)
def forward():
    t.forward(10)
def backward():
    t.forward(-10)
def clock():
    t.right(10)
def anticlock():
    t.left(10)
def col():
    return random.randint(0,255)
def color_change():
    t.color(col(),col(),col())
scr.listen()
scr.onkeypress(key="w" ,fun = forward)
scr.onkeypress(key="s" ,fun = backward)
scr.onkeypress(key="a" ,fun = anticlock)
scr.onkeypress(key="d" ,fun = clock)
scr.onkey(key="space" ,fun = color_change)
scr.exitonclick()
