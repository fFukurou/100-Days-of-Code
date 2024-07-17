#Miles to KM Projet

from tkinter import * #type: ignore

WINDOW_WIDTH = 275
WINDOW_HEIGHT = 100


window = Tk()
window.title("Miles to KM")
window.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
window.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)
window.config(padx=10, pady=5)

def convert():
    miles = float(entry.get())
    return round(miles * 1.60934, 3)

def show_km():
    label_converted_km.config(text=convert())


entry = Entry(width=7)
entry.grid(row=0, column=1)

label_miles = Label(text="Miles", font=("Arial", 15, "italic"))
label_miles.grid(row=0, column= 2)

label_equals = Label(text="is equal to", font=("Arial", 15, "italic"))
label_equals.grid(row=1, column= 0)

label_converted_km = Label(text=f"0", font=("Arial", 15, "italic"))
label_converted_km.grid(row=1, column= 1)

label_km_text = Label(text="Km", font=("Arial", 15, "italic"))
label_km_text.grid(row=1, column= 2)

button = Button(text="Calculate", command=show_km)
button.grid(row=2, column=1)
button.config(padx=10)



window.mainloop()