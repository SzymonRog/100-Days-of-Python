import string
import tkinter
from tkinter import messagebox
import random
import json
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
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")

    if is_ok:
        try:
            file =  open("data.json", "r")
            data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            file.close()
            website_input.delete(0, tkinter.END)
            password_input.delete(0, tkinter.END)




# ---------------------------- Search Website ------------------------------- #
def search_website():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for such website exists!")



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
website_input.grid(column=1, row=1,sticky="we", padx=(0, 20))
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

search_button = tkinter.Button(text="Search", width=15, command=search_website)
search_button.grid(column=2, row=1, sticky="we")

window.mainloop()
