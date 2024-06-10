import tkinter as tk

root = tk.Tk()
root.title("Welcome")


root.geometry("600x400")

menu = tk.Menu(root)
item = tk.Menu(menu)
item.add_command(label="New")
menu.add_cascade(label="File", menu=item)
root.config(menu=menu)


lbl = tk.Label(root, text="Are you a Geek?")
lbl.grid()

# adding Entry Field
txt = tk.Entry(root, width=10)
txt.grid(column=1, row=0)


# function to display user text when
# button is clicked
def clicked():
    res = f"You wrote {txt.get()}"
    lbl.configure(text=res)


# button widget with red color text inside
btn = tk.Button(root, text="Click me", fg="red", command=clicked)
# Set Button Grid
btn.grid(column=2, row=0)

root.mainloop()
