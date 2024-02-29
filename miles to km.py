from tkinter import *


window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=100)
window.config(padx=10, pady=10)


def button_clicked():
    new_text = float(input.get())
    km = new_text * 1.609
    km_result_label.config(text=f"{km}")


# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="Is equal to ")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(anchor="w", justify="left")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button

button = Button(text="Calculate", command=button_clicked)
button.focus_set()
button.grid(column=1, row=2)


# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

window.mainloop()
