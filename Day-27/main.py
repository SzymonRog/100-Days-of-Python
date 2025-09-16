import tkinter
# ---------------Const----------------
RATE = 1.60
# ---------------Window----------------

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=30, pady=30)

# --------------Title Label----------------

my_label = tkinter.Label(text="is equal to")


# -------------Miles to Km Labels-------------

miles_label = tkinter.Label(text="Miles")
miles_label.config(pady=5, padx=5)
miles_label.grid(column=2, row=0)

miles_value_label = tkinter.Label(text="0", font=("Arial", 12, "bold"))
miles_value_label.grid(column=1, row=0)
miles_value_label.config(pady=5 ,padx=5)

kilometers_label = tkinter.Label(text="Kilometers")
kilometers_label.config(pady=5, padx=5)
kilometers_label.grid(column=2, row=1)

kilometers_value_label = tkinter.Label(text="0", font=("Arial", 12, "bold"))
kilometers_value_label.grid(column=1, row=1)
kilometers_value_label.config(pady=5, padx=5)

# -------------Convert functions-------------

global_km = 0
global_miles = 0

def convert_miles():
    global global_km
    try:
        miles = miles_input.get()
        km = round(float(miles) * RATE, 2)
        global_km = km
        kilometers_value_label.config(text=f"{km}")
    except ValueError:
        kilometers_value_label.config(text="Error!")


def convert_kilometers():
    global global_miles
    try:
        km = kilometers_input.get()
        miles = round(float(km) / RATE, 2)
        global_miles = miles
        miles_value_label.config(text=f"{miles}")
    except ValueError:
        miles_value_label.config(text="Error!")


def calculate():
    if radio_state.get() == 1:
        convert_miles()
    else:
        convert_kilometers()

# -------------Convert Inputs and buttons-------------

button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

miles_input = tkinter.Entry(width=20)
miles_input.grid(column=1, row=0)

kilometers_input = tkinter.Entry(width=20)
kilometers_input.grid(column=1, row=1)

# --------------Radio Button ------------
question_label = tkinter.Label(text="Choose a unit you want convert:")
question_label.place(x=40, y=100)


def radio_used():
    global global_km
    global global_miles
    value = radio_state.get()
    if value == 1:
        miles_value_label.grid_remove()
        kilometers_input.grid_remove()
        my_label.grid(column=0, row=1)

        try:
            miles_input.delete(0, tkinter.END)
            miles_input.insert(0, str(global_miles))
        except:
            pass

        miles_input.grid()
        kilometers_value_label.grid()
    else:
        kilometers_value_label.grid_remove()
        miles_input.grid_remove()
        my_label.grid(column=0, row=0)

        try:
            kilometers_input.delete(0, tkinter.END)
            kilometers_input.insert(0, str(global_km))
        except:
            pass

        miles_value_label.grid()
        kilometers_input.grid()

    calculate()


# Variable to hold on to which radio button value is checked.

radio_state = tkinter.IntVar(value=1)
radiobutton1 = tkinter.Radiobutton(text="Miles", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Kilometers", value=2, variable=radio_state, command=radio_used)
radiobutton1.place(x=40, y=120)
radiobutton2.place(x=140, y=120)

radio_used()

window.mainloop()