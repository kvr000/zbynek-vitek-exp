#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import random

COLORS = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple", "Cyan", "Magenta"]
CODE_LENGTH = 5

class MastermindGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Mastermind")

        self.secret_code = [random.choice(COLORS) for _ in range(CODE_LENGTH)]
        print("Secret code (debug):", self.secret_code)  # remove this in finished game

        self.guess_vars = [tk.StringVar(value=COLORS[0]) for _ in range(CODE_LENGTH)]
        self.history_frame = tk.Frame(self.root)
        self.build_interface()

    def build_interface(self):
        tk.Label(self.root, text="Choose your colors:").pack(pady=10)

        input_frame = tk.Frame(self.root)
        input_frame.pack()

        for var in self.guess_vars:
            dropdown = ttk.OptionMenu(input_frame, var, var.get(), *COLORS)
            dropdown.pack(side=tk.LEFT, padx=5)

        tk.Button(self.root, text="Check Guess", command=self.check_guess).pack(pady=10)

        self.history_frame.pack(pady=10)

    def check_guess(self):
        guess = [var.get() for var in self.guess_vars]

        # Child should implement this function
        feedback = self.evaluate_guess(guess)

        self.show_guess(guess, feedback)

    def evaluate_guess(self, guess):
        b = 0
        i = 0

        while i<5:
            if guess[i]==self.secret_code[i]:
                b = b + 1
            i = i + 1
        return ( b, 0)

    def show_guess(self, guess, feedback):
        row = tk.Frame(self.history_frame)
        row.pack(anchor='w')

        for color in guess:
            label = tk.Label(row, text=color[:1], width=2, bg=color.lower(), fg="white")
            label.pack(side=tk.LEFT, padx=2)

        black, white = feedback
        feedback_label = tk.Label(row, text=f"🖤 {black} ⚪ {white}", padx=10)
        feedback_label.pack(side=tk.LEFT)

if __name__ == "__main__":
    root = tk.Tk()
    game = MastermindGame(root)
    root.mainloop()

































