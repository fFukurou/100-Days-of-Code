from tkinter import * # type: ignore

def button_click():
    print("button got clicked")
    my_label['text'] = input.get()



#Window

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height= 300)
window.config(padx=100, pady=200)

#Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))

my_label['text'] = "New Text"
my_label.config(text="New Text V2")
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)

#Button

button1 = Button(text="Click Me", command=button_click)
button1.grid(row=1, column=1)

button2 = Button(text="Click Me Too!", command=button_click)
button2.grid(row=0, column=2)


#Entry

input = Entry(width=10)
input.grid(row=2, column=3)

window.mainloop()