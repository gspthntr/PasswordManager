from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="w")

gen_pass = Button(text="Generate Password", width=14)
gen_pass.grid(column=1, row=3, sticky="e")
add_pass = Button(text="Add", width=29)
add_pass.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
