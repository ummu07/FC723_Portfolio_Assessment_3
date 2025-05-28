#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 23 14:47:14 2025

@author: ummusalmahumarrani
"""
"""
=== FC723 Scientific Calculator (GUI + Console Logic Integration) ===
Author: Ummusalmah (GUI Design & Integration) 
Partner: Lynn (Scientific Logic) 
Description:
- GUI calculator with scientific functionality. 
- Styled to mimic the iPhone calculator.
- Core logic from Lynn's console version adapted into GUI. 
"""

import tkinter as tk # GUI framework 
from tkinter import ttk # For pop-up info box 
import math # Math functions for scientific operations 

# === MAIN WINDOW SETUP ===
root = tk.Tk() # create the main calculator window 
root.title("FC723 Scientific Calculator") # Set window title 
root.geometry("430x900") # Define window size
root.configure(bg="black") # Black background like iPhone calculator 

# === STYLING SETUP ===
style = ttk.Style()
style.theme_use('clam')  # Enables background color control

# Define styles for buttons
style.configure('Orange.TButton', background='#ff9500', foreground='white',
                font=('Helvetica', 22, 'bold'), padding=10)
style.map('Orange.TButton', background=[('active', '#e08600')])

style.configure('Dark.TButton', background='#1c1c1e', foreground='white',
                font=('Helvetica', 22, 'bold'), padding=10)
style.map('Dark.TButton', background=[('active', '#333333')])

style.configure('Gray.TButton', background='#a6a6a6', foreground='black',
                font=('Helvetica', 22, 'bold'), padding=10)
style.map('Gray.TButton', background=[('active', '#8e8e8e')])

# === DISPLAY FIELD ===
entry = tk.Entry(root, font=("Helvetica", 36), justify='right', bg="black",
                 fg="white", insertbackground="white", bd=0, relief='flat')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=30, ipadx=10, ipady=20)

# === CORE FUNCTIONS ===
def press(val):
    entry.insert(tk.END, val)

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def toggle_sign():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, -value)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def insert_result(func):
    try:
        value = float(entry.get())
        result = func(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Domain Err")
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# === SCIENTIFIC FUNCTIONS ===
def sqrt(): insert_result(math.sqrt)
def square(): insert_result(lambda x: x**2)
def sin(): insert_result(lambda x: math.sin(math.radians(x)))
def cos(): insert_result(lambda x: math.cos(math.radians(x)))
def tan(): insert_result(lambda x: math.tan(math.radians(x)))
def arcsin(): insert_result(lambda x: math.degrees(math.asin(x)) if -1 <= x <= 1 else float('nan'))
def arccos(): insert_result(lambda x: math.degrees(math.acos(x)) if -1 <= x <= 1 else float('nan'))
def arctan(): insert_result(lambda x: math.degrees(math.atan(x)))
def log(): insert_result(math.log10)
def ln(): insert_result(math.log)
def insert_pi(): entry.insert(tk.END, str(math.pi))
def insert_e(): entry.insert(tk.END, str(math.e))

# === CREATE BUTTON FUNCTION ===
def create_button(text, row, col, cmd, style_name):
    btn = ttk.Button(root, text=text, style=style_name, command=cmd)
    btn.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)

# === FUNCTION ROW ===
create_button("C", 1, 0, clear, 'Gray.TButton')
create_button("+/-", 1, 1, toggle_sign, 'Gray.TButton')
create_button("%", 1, 2, lambda: None, 'Gray.TButton')
create_button("/", 1, 3, lambda: press("/"), 'Orange.TButton')

# === MAIN BUTTONS ===
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    if text in "+-*/=":
        cmd = equal if text == '=' else lambda t=text: press(t)
        create_button(text, row, col, cmd, 'Orange.TButton')
    else:
        create_button(text, row, col, lambda t=text: press(t), 'Dark.TButton')

# Special case: 0 spans 2 columns
ttk.Button(root, text='0', style='Dark.TButton', command=lambda: press('0')).grid(
    row=5, column=0, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)

# === SCIENTIFIC BUTTONS ===
scientific = [
    ('√x', sqrt), ('x²', square), ('sin', sin), ('cos', cos),
    ('tan', tan), ('arcsin', arcsin), ('arccos', arccos), ('arctan', arctan),
    ('log', log), ('ln', ln), ('π', insert_pi), ('e', insert_e),
]

row, col = 6, 0
for (label, func) in scientific:
    create_button(label, row, col, func, 'Dark.TButton')
    col += 1
    if col > 3:
        col = 0
        row += 1

# === LAUNCH GUI ===
root.mainloop()

