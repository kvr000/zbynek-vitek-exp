import colorsys
import random
import sys
import turtle
from turtle import *
shape("turtle")
speed(3)
pencolor("green")
pensize(6)
Screen().bgcolor("blue")
def hexagon():
    forward(25)
    left(60)
    forward(50)
    left(60)
    forward(50)
    left(60)
    forward(50)
    left(60)
    forward(50)
    left(60)
    forward(50)
    left(60)
    forward(25)


def triangle():
    forward(25)
    left(120)
    forward(50)
    left(120)
    forward(50)
    left(120)
    forward(25)


def square():
    forward(25)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(25)


def rectangle():
    forward(40)
    left(90)
    forward(50)
    left(90)
    forward(80)
    left(90)
    forward(50)
    left(90)
    forward(40)

hexagon()

triangle()

square()

rectangle()








turtle.onscreenclick(lambda x, y: sys.exit(0), 1)
turtle.mainloop()


