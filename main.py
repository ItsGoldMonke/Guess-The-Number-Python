import random
import time
import tkinter as tk
from tkinter import messagebox

class GtnGUI:
        
        # Initializing the GUI
        def __init__(self):
                self.root = tk.Tk()
                self.root.title("Guess The Number Game")
                self.root.geometry("600x300")
                
                self.label = tk.Label(self.root, text="Welcome to the Guess The Number Game!", font=("Helvetica", 16))
                self.label.pack(padx=30, pady=20)

                self.notifylabel = tk.Label(self.root, text="Click the button below to start the game.", font=("Helvetica", 12))
                self.notifylabel.pack(padx=20, pady=10)
                

                self.startbtn = tk.Button(self.root, text="Start Game", command=self.start_game)
                self.startbtn.pack()

                self.root.mainloop()
        
        def start_game(self):
                self.startbtn.pack_forget()
                self.notifylabel.pack_forget()
                self.label.config(text="Enter a minimum and maximum number for the range:")

                self.min_label = tk.Label(self.root, text="Minimum:", font=("Helvetica", 12))
                self.min_label.pack(pady=(10, 0))
                self.min_entry = tk.Entry(self.root)
                self.min_entry.pack()

                self.max_label = tk.Label(self.root, text="Maximum:", font=("Helvetica", 12))
                self.max_label.pack(pady=(10, 0))
                self.max_entry = tk.Entry(self.root)
                self.max_entry.pack()


                self.submitbtn = tk.Button(self.root, text="Submit", command=self.set_range)
                self.submitbtn.pack()

        def set_range(self):
                try:
                    self.min = int(self.min_entry.get())
                except ValueError:
                    self.label.config(text="Please enter valid integers for min and max.")
                    return
                try:
                    self.max = int(self.max_entry.get())
                except ValueError:
                    self.label.config(text="Please enter valid integers for min and max.")
                    return
                if self.min >= self.max:
                    messagebox.showerror("Input Error", "Minimum should be less than maximum. Please try again.")
                    return
                self.guess_number()

        def guess_number(self):
            self.min_entry.pack_forget()
            self.max_entry.pack_forget()
            self.max_label.pack_forget()
            self.min_label.pack_forget()
            self.submitbtn.pack_forget()
            self.notifylabel.pack_forget()
            self.number_to_guess = random.randint(self.min, self.max)
            print(self.number_to_guess)
            self.label.config(text="Random Number Generated, Enter Your Guess:")
            self.guesses = 0
            self.label.pack()

            self.guess_input = tk.Entry(self.root)
            self.guess_input.pack()
            self.guessbtn = tk.Button(self.root, text="Guess", command=self.check_guess)
            self.guessbtn.pack(pady=10)

        def check_guess(self):
            try:
                self.guess = int(self.guess_input.get())
            except ValueError:
                self.label.config(text="Invalid input. Please enter a valid integer (whole number).")
                return
            self.guesses += 1
            if self.guess > self.number_to_guess:
                self.label.config(text="You guessed too high. Try again:")
            elif self.guess < self.number_to_guess:
                self.label.config(text="You guessed too low. Try again:")
            else:
                messagebox.showinfo("Congratulations!", f"You've guessed the number {self.number_to_guess} correctly in {self.guesses} guesses!")
                self.root.destroy()


GtnGUI()

