from tkinter import *


def button_clicked():
    new_text = round(float(entry.get()) * 1.609, 2)
    result_label.config(text=new_text)


miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

is_equal_to_label = Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_to_label.grid(column=0, row=1)

result_label = Label(text="", font=("Arial", 12, "bold"))
result_label.grid(column=1, row=1)

entry = Entry()
entry.grid(column=1, row=0)

button = Button(text="Click on me", command=button_clicked)
button.grid(column=1, row=2)

window = Tk()
window.title("Mile to Km Converter")
window.minsize()

window.mainloop()
