import string
import tkinter
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%"
    password = "".join(random.choice(characters) for _ in range(length))
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()
    return password

def click_generate_password():
    password = generate_password()
    password_input.delete(0, tkinter.END)
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")

    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")

        website_input.delete(0, tkinter.END)
        password_input.delete(0, tkinter.END)




# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(height=200, width=200)
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


# Labels
website_label = tkinter.Label(text="Website:")
website_label.config(pady=3, padx=10)
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_label.config(pady=3, padx=10)

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)
password_label.config(pady=3, padx=10)

# Inputs
website_input = tkinter.Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2,sticky="we")
email_input = tkinter.Entry(width=35)
email_input.insert(0,"szymonrogala78@gmail.com")
email_input.grid(column=1, row=2, columnspan=2,sticky="we")
password_input = tkinter.Entry(width=20)
password_input.grid(column=1, row=3,sticky="we",padx=(0,20))


# Buttons
generate_password_button = tkinter.Button(text="Generate Password", width=15,command=click_generate_password)
generate_password_button.grid(column=2,row=3)


add_button = tkinter.Button(text="Add" ,width=36, command=add_password)
add_button.grid(column=1,row=4,columnspan=2, sticky="we")


window.mainloop()
