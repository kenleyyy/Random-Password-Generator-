# Kenley Hilaire
# May 21, 2024
# Password Generator 


# Project to generate a random password

# Imports libraries 
import random
import string 
import tkinter as tk
from tkinter import messagebox

# Creates function to generate password 
# Can customize if there are numbers or characters included 
def generate_password(min_length, numbers=True, special_characters=True): 
    letters = string.ascii_letters 
    digits = string.digits
    special_chars = string.punctuation
    
    # Creates variable (list) that contains all the characters on a keyboard 
    characters = letters 

    # Checks if numbers or special characters are being used (True or False)
    if numbers:
        characters += digits 
    if special_characters:
        characters += special_chars

    pwd = "" 
    meet_criteria = False 
    has_number = False 
    has_special = False 
    
    # Generates random character from "characters" list
    # While loop to check if password meets the requirements (requirements are when meet_criteria = True) 
    while not meet_criteria or len(pwd) < min_length: 
        new_char = random.choice(characters) 
        pwd += new_char 
        
        # Checks if "new_char" is a special character or a number 
        if new_char in digits:
            has_number = True 
        if new_char in special_chars:
            has_special = True

        # Reset meet_criteria to True at the start of each iteration
        meet_criteria = True 
        if numbers:
            meet_criteria = meet_criteria and has_number 
        if special_characters:
            meet_criteria = meet_criteria and has_special 

    return pwd 

# Creates function to handle button click and retrieve valid user input - outputs messagebox error otherwise
def on_generate_password():
    try:
        min_length = int(min_length_entry.get())
        has_number = numbers_var.get()
        has_special = special_characters_var.get()
        
        pwd = generate_password(min_length, has_number, has_special)
        password_label.config(text=f"Generated Password: {pwd}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for minimum length")

# Creates the main window
root = tk.Tk()
root.title("Welcome to the Password Generator!")

# Creates label  "Minimum Length" and displays in grid 
tk.Label(root, text="Minimum Length:").grid(row=0, column=0, padx=10, pady=10)

# Creates entry widget for user input and displays in the grid 
min_length_entry = tk.Entry(root)
min_length_entry.grid(row=0, column=1, padx=10, pady=10)

# Button Checker to see if numbers will be included and displays in grid accordingly
numbers_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=1, column=0, columnspan=2)

# Button Checker to see if special characters will be included and displays in grid accordingly
special_characters_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Special Characters", variable=special_characters_var).grid(row=2, column=0, columnspan=2)

# Creates password generator button and displays in grid 
generate_button = tk.Button(root, text="Generate Password", command=on_generate_password)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Displays generated password label
password_label = tk.Label(root, text="Generated Password: ")
password_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()