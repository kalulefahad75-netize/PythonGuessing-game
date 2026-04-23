import random    
import tkinter as tk    
from tkinter import messagebox    
    
class GuessingGame:    
    def __init__(self, root):    
        self.root = root    
        self.root.title("Number Guessing Game")    
        self.root.geometry("400x320")   
        self.root.configure(padx=20, pady=20)    
    
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 7
        
        self.create_widgets()    
    
    def create_widgets(self):    
        self.title_label = tk.Label(self.root, text="I'm thinking of a number...", font=("Helvetica", 14, "bold"))    
        self.title_label.pack(pady=(0, 5))    
    
        self.instruction_label = tk.Label(self.root, text=f"Enter a number between 1 and 100\n(7 attempts max)")    
        self.instruction_label.pack()

        
        self.attempt_label = tk.Label(self.root, text=f"Attempts: {self.attempts}/{self.max_attempts}", font=("Helvetica", 10))
        self.attempt_label.pack(pady=5)
    
        # Input Field    
        self.entry = tk.Entry(self.root, font=("Helvetica", 12), justify='center')    
        self.entry.pack(pady=10)    
        self.entry.bind('<Return>', lambda event: self.check_guess())     
        self.entry.focus_set()    
      
        self.button_frame = tk.Frame(self.root)    
        self.button_frame.pack(pady=10)    
        
        self.check_button = tk.Button(self.button_frame, text="Check Guess", command=self.check_guess, bg="#4CAF50", fg="white",     
            font=("Helvetica", 10, "bold"), padx=10, width=12)    
        self.check_button.pack(side=tk.LEFT, padx=5)    
        
        self.reset_button = tk.Button(self.button_frame, text="Reset Game", command=self.reset_game, bg="#f44336", fg="white",    
            font=("Helvetica", 10, "bold"), padx=10, width=12)    
        self.reset_button.pack(side=tk.LEFT, padx=5)    
     
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 10, "italic"))    
        self.result_label.pack(pady=10)    
    
    def check_guess(self):    
        try:    
            guess = int(self.entry.get())    
        except ValueError:    
            messagebox.showwarning("Invalid Input", "Please enter a valid whole number.")    
            return    
    
        self.attempts += 1
        self.attempt_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")

        if guess == self.secret_number:    
            self.result_label.config(text="You got it!", fg="green")    
            messagebox.showinfo("Winner!", f"Correct! The number was {self.secret_number}.\nIt took you {self.attempts} attempts.")    
            self.reset_game()
            return

        # Check if out of attempts
        if self.attempts >= self.max_attempts:
            messagebox.showwarning("Game Over", f"Out of attempts! The number was {self.secret_number}.")
            self.reset_game()
            return

        if guess < self.secret_number:    
            self.result_label.config(text=f"Too low! (Last guess: {guess})", fg="red")    
        elif guess > self.secret_number:    
            self.result_label.config(text=f"Too high! (Last guess: {guess})", fg="red")    
        
        self.entry.delete(0, tk.END)

    def reset_game(self):    
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)    
        self.result_label.config(text="New round! Try again.", fg="blue")
        self.attempt_label.config(text=f"Attempts: 0/{self.max_attempts}")
        self.entry.focus_set()    
    
if __name__ == "__main__":    
    root = tk.Tk()    
    app = GuessingGame(root)    
    root.mainloop()