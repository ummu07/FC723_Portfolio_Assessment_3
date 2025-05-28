#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 23 14:47:14 2025

@author: ummusalmahumarrani
"""

# === FC723 Scientific Calculator (GUI + Console Logic Integration) ===
# Author: Ummusalmah & Lynn
# Description:
# - GUI created by Ummusalmah using Tkinter
# - Scientific function logic adapted from Lynn’s console-based version
# - Styled to match the iPhone calculator (dark theme, orange operators)

import tkinter as tk
from tkinter import messagebox
import math

# === MAIN WINDOW SETUP ===
root = tk.Tk()
root.title("FC723 Scientific Calculator")
root.geometry("430x900")  
root.configure(bg="#000000")  # Dark background for iPhone style

# === DISPLAY FIELD ===
entry = tk.Entry(root, width=14, font=("Helvetica", 36), borderwidth=0,
                 relief="flat", justify="right", bg="#000000", fg="white", insertbackground="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=30)

# === CORE FUNCTIONALITY ===
def press(value):
    """
    Appends number or operator to the entry field.
    This is triggered whenever a button (number/operator) is passed. 
    """
    entry.insert(tk.END, value)

def clear():
    """
    Clears the ecurrent entry input. This is called when 'C' is pressed. 
    """
    entry.delete(0, tk.END)

def equal():
    """
    Evaluates the current expression in the entry fiels. 
    Displays the result, or an error if invalid. 
    """
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error") 
        
def toggle_sign():
    """
    Toggles the sign of the current number from positive to negative and vice versa. 
    """
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, -value) 

def insert_result(func):
    """Apply a math function and display result."""
    try:
        value = float(entry.get())
        result = func(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error") 

# === SCIENTIFIC FUNCTIONS (based on Lynn's logic, adapted to GUI) ===
def sqrt(): insert_result(math.sqrt) # Square root 
def square(): insert_result(lambda x: x ** 2) # Square a number 
def sin(): insert_result(lambda x: math.sin(math.radians(x))) # Sine (in degrees)
def cos(): insert_result(lambda x: math.cos(math.radians(x))) # Cosine (in degrees)
def tan(): insert_result(lambda x: math.tan(math.radians(x))) # Tangent (in degrees)
def arcsin(): insert_result(lambda x: math.degrees(math.asin(x))) # Inverse sine  
def arccos(): insert_result(lambda x: math.degrees(math.acos(x))) # Inverse cosine 
def arctan(): insert_result(lambda x: math.degrees(math.atan(x))) # Inverse tangent 
def log(): insert_result(math.log10) # Log base 10 
def ln(): insert_result(math.log) # Natural logarithm 
def insert_pi(): entry.insert(tk.END, str(math.pi)) # π constant
def insert_e(): entry.insert(tk.END, str(math.e)) # e constant 

def show_info():
    """Shows project and contributor information."""
    messagebox.showinfo("About", "Built by Lynn & Ummusalmah\nGUI by Ummusalmah\nLogic adapted from Lynn’s console calculator")

# === BUTTON CREATOR ===
def styled_button(text, row, col, command, bg_color, fg_color="white"):
    """
    Creates a styled button and places it in the grid.
    Accepts custom background and foreground colors to simulate iPhone UI
    """
    tk.Button(root, text=text, font=("Helvetica", 24, "bold"), width=5, height=2,
              bg=bg_color, fg=fg_color, borderwidth=0, relief="flat",
              highlightthickness=0, command=command).grid(row=row, column=col, padx=6, pady=6)

# === BASIC BUTTONS (NUMBERS AND OPERATORS) ===
basic_buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=', 5, 3),
]

# Add numeric and operator buttons
for (text, row, col) in basic_buttons:
    action = equal if text == '=' else lambda t=text: press(t)
    color = "#ff9500" if text in ['+', '-', '*', '/', '='] else "#505050"
    styled_button(text, row, col, action, color)

# === FUNCTION ROW BUTTONS ===
styled_button('C', 1, 0, clear, "#a6a6a6", fg_color="black") 
styled_button('+/-', 1, 1, toggle_sign, "#a6a6a6", fg_color="black")  
styled_button('%', 1, 2, lambda: None, "#a6a6a6", fg_color="black") #Optional implementation
styled_button('Info', 1, 3, show_info, "#a6a6a6", fg_color="balck") 

# === SCIENTIFIC BUTTONS ===
scientific_buttons = [
    ('√x', sqrt), ('x²', square), ('sin', sin), ('cos', cos),
    ('tan', tan), ('arcsin', arcsin), ('arccos', arccos), ('arctan', arctan),
    ('log', log), ('ln', ln), ('π', insert_pi), ('e', insert_e),
]

sci_row = 6
sci_col = 0
for (label, func) in scientific_buttons:
    styled_button(label, sci_row, sci_col, func, "#1c1c1e")
    sci_col += 1
    if sci_col > 3:
        sci_col = 0
        sci_row += 1

# === START THE APPLICATION ===
root.mainloop()
