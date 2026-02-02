#!/usr/bin/env python3
import random

number = random.randint(1,100)

tries = 10

guess = int(input("guess a number from 1 to 100"))
while guess != number:

    if guess < number:
        print("your number is to small")
        print()
    else:
        print("your number is to high ")
        print()
    if guess != number:
        tries=tries - 1

    if tries > 0 :

        guess = int(input("you have " + str(tries)+" tries left. please try again."))
        print()
    if tries ==0:
        print("You lose!")
        break

if guess == number:
    print("CONGRATULATIONS! CORRECT ANSWER!")
