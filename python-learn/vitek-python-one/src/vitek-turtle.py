#!/usr/bin/env python3

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
    forward(20)


gameOver = False
score = 0
squaresToClear = 0

def play_bombdodger():
    create_bombfield(bombfield)
    window = tkinter.Tk()
    layout_window(window)
    window.mainloop()

bombfield = []
def create_bombfield(bombfield):
    global squaresToClear
    for row in range(0,10):
        rowList = []
        for column in range(0,10):
            if random.randint(1,100) < 20:
                rowList.append(1)
            else:
                rowList.append(0)
                squaresToClear = squaresToClear + 1
        bombfield.append(rowList)

def printfield(bombfield):
    for rowList in bombfield:
        print(rowList)
def on_click(event):
    global score
    global gameOver
    global squaresToClear
    square = event.widget
    row = int (square.grid_info()["row"])
    column = int(square.grid_info()["column"])
    currentText = square.cget("text")
    if gameOver == False:
        if bombfield[row][column] == 1:
            gameOver = True
            square.config(bg = "red")
            print("Game Over! You hit a bomb")
            print("Your score was: ",score)
        elif currentText == "    ":
            square.config(bg = "brown")
            totalBombs = 0
            if row < 9:
                if bombfield[row+1][column] == 1:
                    totalBombs = totalBombs + 1
            if row > 0:
                if bombfield[row-1][column] == 1:
                    totalBombs = totalBombs + 1
            if column > 0:
                if bombfield[row][column-1] == 1:
                    totalBombs = totalBombs + 1
            if column < 9 :
                if bombfield[row][column+1] == 1:
                    totalBombs = totalBombs + 1
            if row > 0 and column > 0:
                if bombfield[row-1][column-1] == 1:
                    totalBombs = totalBombs + 1
            if row < 9 and column > 0:
                if bombfield[row+1][column-1] == 1:
                    totalBombs = totalBombs + 1
            if row > 0 and column < 9:
                if bombfield[row-1][column+1] == 1:
                    totalBombs = totalBombs + 1
            if row < 9  and column < 9:
                if bombfield[row+1][column+1] == 1:
                    totalBombs = totalBombs + 1
            square.config(text =" " + str(totalBombs) + " ")
            squaresToClear = squaresToClear - 1
            score = score +1
            if squaresToClear == 0:
                gameOver = True
                print("Well done! You found all the safe squares!")
                print("Your score was:", score)

def layout_window(window):
    for rowNumber, rowList in enumerate(bombfield):
        for columnNumber, columnEntry in enumerate(rowList):
            if random.randint(1,100) < 25:
                square = tkinter.Label(window, text = "    ", bg = "darkgreen")
            elif random.randint(1,100) > 75:
                square = tkinter.Label(window, text = "    ", bg = "seagreen")
            else:
                square = tkinter.Label(window, text = "    ", bg = "green")
            square.grid(row = rowNumber, column = columnNumber)
            square.bind("<Button-1>", on_click)













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










turtle.onscreenclick(lambda x, y: sys.exit(0), 1)
turtle.mainloop()


