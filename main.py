#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
"""
GPA CALC WITH TKINTER
Published under the MIT License
Copyright (c) 2022 Austen Sparks
> https://github.com/asparkswghs/tkinter-gpa-calc
NOTE: The 7 periods is hardcoded. sorry.
"""


# GPA function
def gpa():
    # retrieve
    grades = []
    grades.append(entry1.get())
    grades.append(entry2.get())
    grades.append(entry3.get())
    grades.append(entry4.get())
    grades.append(entry5.get())
    grades.append(entry6.get())
    grades.append(entry7.get())

    # convert
    gpas = []
    error_occured = False
    error_in = ''
    for grade in grades:
        grade = grade.lower()

        # letter to points
        if grade == "a" or grade == "a-":
            gpas.append(4.0)
        elif grade == "b+":
            gpas.append(3.5)
        elif grade == "b":
            gpas.append(3.0)
        elif grade == "c+":
            gpas.append(2.5)
        elif grade == "c":
            gpas.append(2.0)
        elif grade == "d" or grade == "d-":
            gpas.append(1.0)
        elif grade == "f":
            gpas.append(0.5)
        else:# check for invalid input
          error_occured = True
          if error_in != '':
            error_in += "', '" + grade
          else:
            error_in += grade
            
         
    if error_occured:
        # PEBKAC: 'Problem Exists Between Keyboard And Chair'
        # See: https://en.wiktionary.org/wiki/PEBCAK
        messagebox.showerror("PEBKAC ERROR!", f'Input \'{error_in}\' is invalid.\nPlease Try Again.')
        return
    
    # calculate
    try:
        gpa_calc = ( sum(gpas) ) / 7
        gpa_is = round(gpa_calc, 2)
    except BaseException as ex:
        messagebox.showerror("Error In Calculating Final GPA", f"Error:\n{ex}")
        return
    
    # display
    gpa_show = tk.Label(text=f'GPA: {gpa_is}')
    gpa_show.grid(row=8,column=2
)




# Window setup
window = tk.Tk()
window.title("GPA Calculator")
window.geometry("350x250")

greeting = tk.Label(text="Calculate Your Grade Point Average")
greeting.grid(row=0,column=0)

button = tk.Button(
    text ="Calculate!",
    fg="white",
    bg="blue",
    width=10,
    height=1,
    command=gpa
)
button.grid(row=8,column=0)

# Entries
entry1 = tk.Entry()
entry1.grid(row=1,column=2)

entry2 = tk.Entry()
entry2.grid(row=2,column=2)

entry3 = tk.Entry()
entry3.grid(row=3,column=2)

entry4 = tk.Entry()
entry4.grid(row=4,column=2)

entry5 = tk.Entry()
entry5.grid(row=5,column=2)

entry6 = tk.Entry()
entry6.grid(row=6,column=2)

entry7 = tk.Entry()
entry7.grid(row=7,column=2)

# Labels
for i in range(7):
    label1 = tk.Label(text=f'Period {i + 1}')
    label1.grid(row=(i + 1),column=0)


# Main Window Loop
window.mainloop()
