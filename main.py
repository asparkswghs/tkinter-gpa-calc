import tkinter as tk
from tkinter import messagebox

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
    for grade in grades:
        grade = grade.lower()

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
        else:
            error_occured = True
    if error_occured:
        messagebox.showerror("Invalid Input!", "This program only accepts standard letter grades.")
        return
    
    # calculate
    try:
        gpa_calc = ( sum(gpas) ) / 7
        gpa_is = round(gpa_calc, 2)
    except BaseException as ex:
        messagebox.showerror("Error In Calculating Final GPA", f"Error:\n{ex}")
    
    # display
    gpa_show = tk.Label(text=f'GPA: {gpa_is}')
    gpa_show.grid(row=8,column=1)




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
entry1.grid(row=1,column=1)

entry2 = tk.Entry()
entry2.grid(row=2,column=1)

entry3 = tk.Entry()
entry3.grid(row=3,column=1)

entry4 = tk.Entry()
entry4.grid(row=4,column=1)

entry5 = tk.Entry()
entry5.grid(row=5,column=1)

entry6 = tk.Entry()
entry6.grid(row=6,column=1)

entry7 = tk.Entry()
entry7.grid(row=7,column=1)

# Labels
for i in range(7):
    label1 = tk.Label(text=f'Period {i + 1}')
    label1.grid(row=(i + 1),column=0)

window.mainloop()
