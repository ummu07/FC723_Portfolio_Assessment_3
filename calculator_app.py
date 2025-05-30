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

import tkinter as tk
from tkinter import ttk
import math

# === MAIN WINDOW SETUP ===
root = tk.Tk()
root.title("FC723 Scientific Calculator")
root.geometry("430x950")  # Increased height for expression display
root.configure(bg="black")  # Set the background color for iPhone-style UI

# === STYLING SETUP ===
style = ttk.Style()
style.theme_use('clam')  # Enables custom background coloring for buttons

# Define iPhone-style button themes
style.configure('Orange.TButton', background='#ff9500', foreground='white',
                font=('Helvetica', 22, 'bold'), padding=10)
style.map('Orange.TButton', background=[('active', '#e08600')])

style.configure('Dark.TButton', background='#1c1c1e', foreground='white',
                font=('Helvetica', 22, 'bold'), padding=10)
style.map('Dark.TButton', background=[('active', '#333333')])

style.configure('Gray.TButton', background='#a6a6a6', foreground='black',
                font=('Helvetica', 22, 'bold'), padding=10)
style.map('Gray.TButton', background=[('active', '#8e8e8e')])

# === EXPRESSION LABEL (New) ===
# This label shows the expression above the main entry display
expression_var = tk.StringVar()
expression_label = tk.Label(root, textvariable=expression_var, font=("Helvetica", 18),
                            fg="white", bg="black", anchor='e')
expression_label.grid(row=0, column=0, columnspan=4, sticky="we", padx=10)

# === DISPLAY FIELD ===
entry = tk.Entry(root, font=("Helvetica", 36), justify='right', bg="black",
                 fg="white", insertbackground="white", bd=0, relief='flat')
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=20)

# === CORE FUNCTIONS ===
def press(val):
    """Appends characters (numbers/operators) to the display."""
    entry.insert(tk.END, val)

def clear():
    """Clears all content from the display field and expression label."""
    entry.delete(0, tk.END)
    expression_var.set("")

def equal():
    """Evaluates the input expression and shows result. Shows error if invalid."""
    try:
        expression = entry.get()
        result = eval(expression.replace('÷', '/'))  # Replace division symbol for eval
        expression_var.set(f"{expression} =")
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def toggle_sign():
    """Toggles the sign of the number from positive to negative and vice versa."""
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, -value)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def insert_result(func):
    """Calls scientific function with input value and displays result."""
    try:
        value = float(entry.get())
        result = func(value)
        expression_var.set(f"{func.__name__}({value}) =")
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Domain Err")  # e.g., asin(2) or log(-1)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# === SCIENTIFIC FUNCTIONS ===
# The following logic was **adapted directly from Lynn’s console-based app**.
def sqrt(): insert_result(math.sqrt)                  # Square root
def square(): insert_result(lambda x: x**2)           # Square
def sin(): insert_result(lambda x: math.sin(math.radians(x)))   # Sine (degrees)
def cos(): insert_result(lambda x: math.cos(math.radians(x)))   # Cosine (degrees)
def tan(): insert_result(lambda x: math.tan(math.radians(x)))   # Tangent (degrees)

# Adapted from Lynn’s domain-safe inverse trig logic:
def arcsin(): insert_result(lambda x: math.degrees(math.asin(x)) if -1 <= x <= 1 else float('nan'))
def arccos(): insert_result(lambda x: math.degrees(math.acos(x)) if -1 <= x <= 1 else float('nan'))
def arctan(): insert_result(lambda x: math.degrees(math.atan(x)))

def log(): insert_result(math.log10)      # Base-10 logarithm
def ln(): insert_result(math.log)         # Natural log
def insert_pi(): entry.insert(tk.END, str(math.pi))  # Insert π
def insert_e(): entry.insert(tk.END, str(math.e))    # Insert Euler’s number

# === CREATE BUTTON FUNCTION ===
def create_button(text, row, col, cmd, style_name):
    """Creates and places a styled ttk.Button on the grid."""
    btn = ttk.Button(root, text=text, style=style_name, command=cmd)
    btn.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)

# === FUNCTION ROW (Top row: Clear, Sign, %, ÷) ===
create_button("C", 2, 0, clear, 'Gray.TButton')
create_button("+/-", 2, 1, toggle_sign, 'Gray.TButton')
create_button("%", 2, 2, lambda: None, 'Gray.TButton')  # Placeholder
create_button("÷", 2, 3, lambda: press("÷"), 'Orange.TButton')  # Division symbol

# === MAIN BUTTONS ===
buttons = [
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
    ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
    ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3),
    ('0', 6, 0), ('.', 6, 1), ('=', 6, 2)
]

# Loop through main buttons and add them to the GUI
for (text, row, col) in buttons:
    if text in "+-*/=":
        cmd = equal if text == '=' else lambda t=text: press(t)
        create_button(text, row, col, cmd, 'Orange.TButton')  # Operators styled orange
    else:
        create_button(text, row, col, lambda t=text: press(t), 'Dark.TButton')  # Numbers styled dark

# Special case: 0 spans 1 column (you may update to 2 if needed)
ttk.Button(root, text='0', style='Dark.TButton', command=lambda: press('0')).grid(
    row=6, column=0, columnspan=1, padx=5, pady=5, ipadx=10, ipady=10)

# === SCIENTIFIC BUTTONS (Extra row) ===
# This section reflects **Lynn’s contribution** turned into GUI form.
scientific = [
    ('√x', sqrt), ('x²', square), ('sin', sin), ('cos', cos),
    ('tan', tan), ('arcsin', arcsin), ('arccos', arccos), ('arctan', arctan),
    ('log', log), ('ln', ln), ('π', insert_pi), ('e', insert_e),
]

row, col = 7, 0
for (label, func) in scientific:
    create_button(label, row, col, func, 'Dark.TButton')
    col += 1
    if col > 3:
        col = 0
        row += 1

# === START GUI LOOP ===
root.mainloop()
