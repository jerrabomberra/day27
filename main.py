from tkinter import *

window = Tk()
window.title("My first GUI")
window.minsize(width=600, height=400)

#label

my_label = Label(font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New text"


# button
def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())
    

button = Button(text="click me", command= button_clicked)
button.pack()

# entry
input = Entry(width = 10)
input.pack()
input.get()



window.mainloop()
