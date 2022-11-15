from tkinter import *

window = Tk()
window.title("Mile to Km")
window.config(padx=50, pady=20)

def miles_to_km():
    miles = float(input.get())
    km = round(miles * 1.609, 2)
    label_result.config(text=f"{km}")

label_equal = Label(text="is equal to")
label_equal.grid(row=1, column=0)

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

label_km = Label(text="Km")
label_km.grid(row=1, column=2)

label_result = Label(text="0")
label_result.grid(row=1, column=1)

input = Entry(width=10)
input.grid(row=0, column=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

window.mainloop()