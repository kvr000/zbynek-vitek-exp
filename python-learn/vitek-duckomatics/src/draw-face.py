#!/usr/bin/env python3

from py5 import *

screen_size = 400

def settings():
    size(screen_size, screen_size)

def setup():
    # Put code to run once here
    rect_mode(CENTER)
    no_stroke()

def draw():
    # Put code to run every frame here
    background(0, 0, 0)
    # Add code to draw your face here
    fill(225, 225, 0)
    rect(
        screen_size/2,
        screen_size/2,
        300,
        300
    )
    fill(0, 0, 0)
    rect(
        120,
        150,
        100,
        80
    )
    fill(0, 0, 0)
    rect(
        290,
        150,
        100,
        80
    )
    fill(0, 0, 225)
    rect(
        208,
        screen_size/2,
        40,
        80
    )

    fill(225, 0, 0)
    triangle(
        240, 100,
        240, 200,
        380, 80
    )
    fill(225, 0, 0)
    triangle(
        175, 100,
        175, 200,
        35, 80
    )
    fill(0, 0, 0)
    rect(
        screen_size/2,
        300,
        250,
        50
    )

print("HELLO!!!")

# Keep this to run your code
run_sketch()
