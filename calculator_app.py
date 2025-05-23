#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 23 14:47:14 2025

@author: ummusalmahumarrani
"""

# === FC723 Scientific Calculaor Application ===
# Author: Ummusalmah (Group with Lynn)
# Description: A GUI calculator using Tkinter with basic and scientific functions. 

import tkinter as tk 
import math 

# === MAIN WINDOW SETUP ===
root = tk.Tk()
root.title("FC723 Scientific Calculator")
root.geometry("400x850")
root.configure(bg="#1c11c1e") # Dark mode backgroud 

# === DISPLAY ENTRY FIELD ===
entry = tk.Entry(root, width=17, font=("Helvetica", 32), borderwidth=0, relief="flat", justify="right", bg="1c1c1e", fg="White")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=30)

# === BASIC INPUT FUNCTIONS ===
def press(value):
    """Appends input value to the entry field."""
    entry.insert(tk.END, value)
    
def clear():
    """Clears the entire entry field."""
    entry.delete(0, tk.END)
    
def equal():
    """Evaluates the expression entered and displays the result."""
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        
# === SCIENTIFIC FUNCTION HANDLERS ===
def sqrt(): entry.insert_result(math.sqrt)
def square(): entry.insert_result(lambda x: x**2)
def sin(): entry.insert_result(math.sin)
def cos(): entry.insert_result(math.cos)
def tan(): entry.insert_result(math.tan)
def arcsin(): entry.insert_result(math.asin)
def arccos(): entry.insert_result(math.acos)
def arctan(): entry.insert_result(math.atan)
def log(): entry.insert_result(math.log10)
def ln(): entry.insert_result(math.log)
def insert_pi(): entry.insert_result(tk.END, str(math.pi))
def insert_e(): entry.insert(tk.END, str(math.e)) 

def insert_result(func):
    try:
        value = float(entry.get())
        result = func(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

entry.insert_result = insert_result 

# === BUTTON STYLE FUNCTION ===
def styled_button(text, roow, col, command, bg_color, fg_color="white"):
    tk.Button(root, text=text, font=("Helvetica", 20), width=5, height=2,
              bg=bg_color, fg=fg_color, borderwidth=0, relief="flat",
              command=command).grid(row=row, column=col, padx=5, pady=5) 

# === BASIC BUTTONS SETUP ===
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
  ] 

for (text, row, col) in buttons: 
    action = equal if text == '=' else lambda t=text: press(t)
    styled_button(text, row, col, action, "#ff9500") if text in ['+', '-', '*', '/', '='] else styled_button(text, row, col, action, "#505050")
    
# === CLEAR BUTTON ===
styled_button('C', 5, 0, clear, "#a6a6a6") 

# === SCIENTIFIC BUTTONS (Row 6 and below) ===
scientific_buttons = [
    ('√x', sqrt), ('x²', square), ('sin', sin), ('cos', cos),
    ('tan', tan), ('arcsin', arcsin), ('arccos', arccos), ('arctan', arctan),
    ('log', log), ('ln', ln), ('π', insert_pi), ('e', insert_e)
]

# Adjust starting row and make sure the layout doesn't clash with basic buttons
sci_row = 6
sci_col = 0
for (label, func) in scientific_buttons:
    styled_button(label, sci_row, sci_col, func, "#3a3a3c")
    sci_col += 1
    if sci_col > 3:
        sci_col = 0
        sci_row += 1
          
# === MAIN LOOP === 
root.mainloop()  
