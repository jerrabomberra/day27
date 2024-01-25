import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=600, height=400)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(padx=50, pady=50)


menu = tkinter.Menu(window)
item = tkinter.Menu(menu)
item.add_command(label="New")
item.add_command(label="Exit")
menu.add_cascade(label="File", menu=item)
window.config(menu=menu)


def clicked():
    res = f"You wrote {txt.get()}"
    my_label.configure(text=res)


# button widget with red color text inside
my_button = tkinter.Button(window, text="Click me", fg="red", command=clicked)
# Set Button Grid
my_button.pack()


window.mainloop()
