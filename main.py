from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- SEARCH WEBSITE ------------------------------- #


def search_site():
    website = web_entry.get().lower()
    try:
        with open("password_manager.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("password_manager.json", mode="w") as file:
            json.dump({}, file)
            messagebox.showinfo(title="File not found", message="No data file found. Creating new JSON file")
    else:
        # Existence of website can be checked with:
        #if website in data: ...

        try:
            with open("password_manager.json", mode="r") as file:
                data = json.load(file)
                email = data[website]["email"]
                password = data[website]["password"]
        except KeyError:
            messagebox.showwarning("Website not found", "No details for the website exists")
        else:
            messagebox.showinfo(website, f"Email: {email}\nPassword: {password}")
            pyperclip.copy(password)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():
    password_entry.delete(first=0, last="end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, string=password)
    pyperclip.copy(password)
    print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = web_entry.get().lower()
    user = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": user,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0 or len(user) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # with open("password_manager.txt", mode="r") as r_file:
        #     r_data = r_file.readlines()
        #     website_exists = any(line.split(" | ")[0] == website for line in r_data)
        #     if not website_exists:
        try:
            with open("password_manager.json", mode="r") as json_file:
                # new_website = f"{website} | {user} | {password}"
                data = json.load(json_file)
                print(data)
        except FileNotFoundError as error_message:
            print(f"That file does not exist{error_message}\nCreating new file")
            with open("password_manager.json", mode="w") as json_file:
                json.dump(new_data, json_file, indent=4)
        except JSONDecodeError as error:
            print(f"ERROR MESSAGE: {error}")
            with open("password_manager.json", mode="w") as json_file:
                json.dump(new_data, json_file, indent=4)
        else:
            data.update(new_data)
            with open("password_manager.json", mode="r+") as json_file:
                json.dump(data, json_file, indent=4)
                print("Website has been added")
        finally:
            web_entry.delete(first=0, last="end")
            password_entry.delete(first=0, last="end")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(width=700, height=700, padx=20, pady=20)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

canvas = Canvas(width=200, height=200)
canvas.config()
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website: ")
web_label.grid(column=0, row=1)
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2, sticky="w")
web_entry.focus()


username_label = Label(text="Email/Username: ")
username_label.grid(column=0, row=2)
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2, sticky="w")
username_entry.insert(0, "default_email@gmail.com")

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="w")

gen_pass = Button(text="Generate Password", width=14, command=gen_password)
gen_pass.grid(column=1, row=3, sticky="e")
add_pass = Button(text="Add", width=29, command=save_password)
add_pass.grid(column=1, row=4, columnspan=2, sticky="w")

search = Button(text="Search", width=14, command=search_site)
search.grid(column=1, row=1, sticky="e")


window.mainloop()
