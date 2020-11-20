import sys, random
import tkinter as tk
from tkinter import ttk
import pyperclip
import re

class GUI():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Python Password Generator")
        self.win.resizable(False, False)
        self.intvar = tk.IntVar()
        self.stringvar = tk.StringVar()
        self.include_numbers = tk.IntVar()
        self.include_symbols = tk.IntVar()
        self.include_lowercase = tk.IntVar()
        self.include_uppercase = tk.IntVar()

        self.add_widgets()

    def add_widgets(self):
        labels = ["Password Length: ", "Include Symbols: ", 
        "Include Numbers: ", "Include Lowercase Characters",
        "Include Uppercase Characters"]

        checkbox_text = ["(e.g. @#$%)", "(e.g. 123456)", "(e.g. abcdefgh)",
        "(e.g. ABCDEFGH)"]

        # adding the labels in a loop
        for i in range(len(labels)):
            # adding labels
            label = ttk.Label(self.win, text=labels[i])
            label.grid(row=i, column=0)

            # adding the password length combobox on the first row
            if i == 0:
                number_of_chars = ttk.Combobox(self.win, width=12, textvariable=self.intvar)
                number_of_chars['values'] = tuple(range(6, 33))
                number_of_chars.grid(column=1, row=0)
                number_of_chars.current(0)
            
            # adding check buttons and text on subsequent rows
            else:
                if i-1 == 0:
                    checkbox = tk.Checkbutton(self.win, text=checkbox_text[i-1], variable=self.include_symbols)
                elif i-1 == 1:
                    checkbox = tk.Checkbutton(self.win, text=checkbox_text[i-1], variable=self.include_numbers)
                elif i-1 == 2:
                    checkbox = tk.Checkbutton(self.win, text=checkbox_text[i-1], variable=self.include_lowercase)
                elif i-1 == 3:
                    checkbox = tk.Checkbutton(self.win, text=checkbox_text[i-1], variable=self.include_uppercase)
                checkbox.grid(row=i, column=1)
        
        i = i+1
        # adding generate password button
        button = tk.Button(self.win, text="Generate Password", command=self.generate_password)
        button.grid(column=1, row=i)

        # adding text field that will contain the generated password
        label = ttk.Label(self.win, text="Your New Password:")
        label.grid(row=i+1, column=0)
        generated_password = ttk.Entry(self.win, width=24, textvariable=self.stringvar)
        generated_password.grid(column=1, row=i+1)
        copy_button = tk.Button(self.win, text="Copy", command=lambda: pyperclip.copy(self.stringvar.get()) )
        copy_button.grid(column=2, row=i+1)

    def generate_password(self):
        ascii_set = [f for f in range(128) if f not in range(0, 32) and f != 127]
        space_regex = re.compile(r'\s')
        lowercase_regex = re.compile('[a-z]')
        uppercase_regex = re.compile('[A-Z]')
        symbol_regex = re.compile(r'[-!@#$%^&*()_+=/.,"<>~`]')
        number_regex = re.compile(r'\d')

        length = self.intvar.get()  # getting the length of the password
        password = ''

        for i in range(length):
            char = chr(random.choice(ascii_set))
            while True:
                if space_regex.search(char):
                    char = chr(random.choice(ascii_set))
                    continue
                elif not self.include_lowercase and lowercase_regex.search(char):
                    char = chr(random.choice(ascii_set))
                    continue
                elif not self.include_numbers and number_regex.search(char):
                    char = chr(random.choice(ascii_set))
                    continue
                elif not self.include_symbols and number_regex.search(char):
                    char = chr(random.choice(ascii_set))
                    continue
                elif not self.include_uppercase and uppercase_regex.search(char):
                    char = chr(random.choice(ascii_set))
                    continue
                else:
                    password = password + char
                    break
        
        self.stringvar.set(password)

gui = GUI()
gui.win.mainloop()