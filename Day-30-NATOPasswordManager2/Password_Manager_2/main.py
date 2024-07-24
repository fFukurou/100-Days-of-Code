#Password Manager Project 2
#Added search function with error handling

from textwrap import indent
from tkinter import * #type: ignore
from tkinter import messagebox
import random
from webbrowser import get
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbol_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    number_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    random.shuffle(password_list)

    """ password = ""
    for char in password_list:
    password += char """

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    if entry_website.get() == "" or entry_emailusername.get() == "" or entry_password.get() == "":
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
        

    else: 
        website = entry_website.get().upper()
        email = entry_emailusername.get()
        password = entry_password.get()

        new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }
        try:
            with open(f"Day-30-NATOPasswordManager2/Password_Manager_2/data.json", "r") as file:
                # Reading old data
                data = json.load(file)
                # Updading old data
                data.update(new_data)

        except FileNotFoundError:
            with open(f"Day-30-NATOPasswordManager2/Password_Manager_2/data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            with open(f"Day-30-NATOPasswordManager2/Password_Manager_2/data.json", "w") as file:
                # Saving old data
                json.dump(data, file, indent=4)

        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search():
    site = entry_website.get().upper()
    try:
        with open(f"Day-30-NATOPasswordManager2/Password_Manager_2/data.json", "r") as file:
            data = json.load(file)

        messagebox.showinfo(title=site.capitalize() + " password", message=f"Site: {site.capitalize()}\nPassword: {data[site]['password']}")

    except FileNotFoundError:
        messagebox.showinfo(title="404 File Not Found", message=f"No Data File Found")
    
    except KeyError:
        messagebox.showinfo(title="Site not found", message=f"No details for the website exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="Day-30-NATOPasswordManager2/Password_Manager_2/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
entry_website = Entry()
entry_website.grid(row=1, column=1, sticky="EW")
entry_website.focus()

button_search = Button(text="Search", command=search)
button_search.grid(row=1, column=2, sticky="EW")

label_emailusername = Label(text="Email/Username:")
label_emailusername.grid(row=2, column=0)
entry_emailusername = Entry()
entry_emailusername.grid(row=2, column=1, columnspan=2, sticky="EW")
entry_emailusername.insert(END, "dummyemail@gmail.com")

label_password = Label(text="Password:")
label_password.grid(row=3, column=0)
entry_password = Entry()
entry_password.grid(row=3, column=1, sticky="EW")

button_generate_password = Button(text="Generate Password", command=generate_password)
button_generate_password.grid(row=3, column=2, sticky="EW")

button_add = Button(text="Add", width=35, command=save)
button_add.grid(row=4, column=1, columnspan=2, sticky="EW")
 

window.mainloop()   