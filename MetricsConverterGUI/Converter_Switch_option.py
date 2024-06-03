from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(300, 200)
window.config(padx=20, pady=20)

# Labels
input_label = Label(text="Miles")
input_label.grid(column=3, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=1, row=1)

result_label = Label(text="0")
result_label.grid(column=2, row=1)

result_unit_label = Label(text="KM")
result_unit_label.grid(column=3, row=1)

# Entry
input = Entry(width=10)
input.grid(column=2, row=0)

# Variables to track the conversion direction
convert_to_km = True

def button_clicked():
    new_label = input.get()
    try:
        value = float(new_label)
        if convert_to_km:
            calculate = value * 1.609
            result_label.config(text=f"{calculate:.2f}")
        else:
            calculate = value / 1.609
            result_label.config(text=f"{calculate:.2f}")
    except ValueError:
        result_label.config(text="Invalid Input")

def switch_conversion():
    global convert_to_km
    convert_to_km = not convert_to_km
    if convert_to_km:
        input_label.config(text="Miles")
        result_unit_label.config(text="KM")
    else:
        input_label.config(text="KM")
        result_unit_label.config(text="Miles")
    result_label.config(text="0")
    input.delete(0, END)

# Calculate Button
calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=2, row=2)  # Placing the button in grid

# Switch Button
switch_button = Button(text="Switch Conversion", command=switch_conversion)
switch_button.grid(column=2, row=3)  # Placing the switch button in grid

window.mainloop()
