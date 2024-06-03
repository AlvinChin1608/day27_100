import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
#my_label.place(x=200, y=300)
my_label.grid(column=0, row=0)  # Placing the label in grid

my_label["text"] = "New Text"
my_label.config(text="New Text")  # does the same as above

# Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)  # Placing the button in grid

button1 = tkinter.Button(text="Click Me", command=button_clicked)
button1.grid(column=3, row=0)  # Placing the button in grid

# Entry
input = tkinter.Entry(width=10)
input.grid(column=2, row=2)  # Placing the entry in grid

print(input.get())

window.mainloop()
