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
    new_text=input.get()
    my_label.config(text=new_text)
    

button = Button(text="click me", command= button_clicked)
button.pack()

# entry
input = Entry(width = 10, font=("Arial", 24, "bold"))
input.pack(padx=10, pady=10)
input.get()



window.mainloop()
