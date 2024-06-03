
from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(300,150)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="is equal to")
my_label.grid(column = 1, row = 1)

my_label = Label(text="Miles")
my_label.grid(column = 3, row = 0)

my_label = Label(text="KM")
my_label.grid(column = 3, row = 1)

result_label = Label(text="0")
result_label.grid(column = 2, row = 1)

# Entry
input = Entry(width=5)
input.grid(column= 2, row = 0)

def button_clicked():
    new_label = input.get()
    calculate = float(new_label)*1.609
    result_label.config(text=f"{calculate}") # Update result_label with calculated value
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)  # Placing the button in grid



window.mainloop()
