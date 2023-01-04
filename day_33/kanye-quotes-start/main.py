from tkinter import *
import requests
import textwrap

FONT_NAME = "Courier"
ENDPOINT = "https://api.kanye.rest"


def get_kanye_qoute():
    qoute = requests.get(ENDPOINT).json()['quote']
    canvas.itemconfig(kanye_text, text=textwrap.fill(qoute, 18))


window = Tk()
window.title("kanye says")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=300, height=414, highlightthickness=0, bg="white")
photo = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=photo)
kanye_text = canvas.create_text(150, 207, text="kanye Says", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.pack()

button_photo = PhotoImage(file="kanye.png")
reset_button = Button(image=button_photo, highlightthickness=0, command=get_kanye_qoute, bg="white")
reset_button.pack()

get_kanye_qoute()

window.mainloop()
