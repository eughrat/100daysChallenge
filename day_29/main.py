from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip

letters_lower = [i for i in string.ascii_lowercase]
letters_upper = [i for i in string.ascii_uppercase]
digits = [i for i in string.digits]
punctuation = [i for i in string.punctuation]


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    let_low = random.choices(letters_lower, k=3)
    let_up = random.choices(letters_upper, k=3)
    dig = random.choices(digits, k=3)
    punc = random.choices(punctuation, k=3)
    password = let_low + let_up + dig + punc
    random.shuffle(password)
    password = ''.join(password)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    if len(website_input.get()) == 0 or len(password_input.get()) == 0 or len(username_input.get()) == 0:
        messagebox.showinfo(title="Alert!",
                            message=f"There are blanks left to fill in!")
    else:
        is_ok = messagebox.askquestion(title=website_input.get(),
                                       message=f"These are the details entered: \nEmail: {username_input.get()}"
                                               f" \nPassword: {password_input.get()} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website_input.get()} | {username_input.get()} | {password_input.get()}\n")
            website_input.delete(0, 'end')
            password_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

# LABELS
website_label = Label(text="Website")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username")
username_label.grid(column=0, row=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

# ENTRIES
website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "michal.piernicki@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# BUTTONS
generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
