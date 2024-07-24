#Password Manager Project
from tkinter import * #type: ignore
from tkinter import messagebox
import random
import pyperclip


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
        is_ok = messagebox.askokcancel(title=entry_website.get(), message=f"These are the details entered: \n\nEmail: {entry_emailusername.get()}\n\nPassword: {entry_password.get()}\n\nIs it ok to save?")
        
        if is_ok:
            with open(f"Day-29-PasswordManager/Password_Manager_1/data.txt", "a") as file:
                file.write(f"{entry_website.get()} | {entry_emailusername.get()} | {entry_password.get()}\n")
            
            entry_website.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="Day-29-PasswordManager/Password_Manager_1/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
entry_website = Entry()
entry_website.grid(row=1, column=1, columnspan=2, sticky="EW")
entry_website.focus()

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