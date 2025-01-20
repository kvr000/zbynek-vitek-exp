
print("pick a shape")
print("1 is a spiral")
print("2 is a hexagon")
print("3 is a triangle")
print("4 is a rectangle")
print("5 is a square")








playerChoice=input("choose 1,2,3,4 or 5")
playerChoice = playerChoice.strip()

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

def spiral():
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(90)
    right(90)
    forward(90)
    right(90)
    forward(80)
    right(90)
    forward(80)
    right(90)
    forward(70)
    right(90)
    forward(70)
    right(90)
    forward(60)
    right(90)
    forward(60)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(40)
    right(90)
    forward(40)
    right(90)
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(20)
    right(90)
    forward(20)
    right(90)
    forward(10)
    right(90)
    forward(10)
    hideturtle()

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

def square():
    forward(40)
    right(90)
    forward(40)
    right(90)
    forward(40)
    right(90)
    forward(40)
    right(90)









def spiral2():
   step = 100
   while step > 0:
      forward(step)
      right(90)
      forward(step)
      right(90)
      forward(step)
      right(90)
      step = step - 10
   #   forward(step)
     # right(90)

if playerChoice == "1":
    spiral2()

elif playerChoice == "2":
    hexagon()

elif playerChoice == "3":
    triangle()

elif playerChoice == "4":
    rectangle()

elif playerChoice == "5":
    square()



turtle.onscreenclick(lambda x, y: sys.exit(0), 1)
turtle.mainloop()

