import tkinter
from tkinter import PhotoImage

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    checkmarks.config(text=calc_checkmarks())

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(3)

    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(3)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    canvas.itemconfig(timer_text, text=f"{count // 60:02d}:{count % 60:02d}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)

    if count == 0:
        start_timer()







# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Title
title_label = tkinter.Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

# Tomato img
canvas = tkinter.Canvas(width=200, height=224 ,bg=YELLOW, highlightthickness=0)
tomato_img =  PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)



# Buttons
start_button = tkinter.Button(width=5,text="Start", bg="white", font=( "Inter", 12, "normal"), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(width=5,text="Reset", bg="white", font=( "Inter",12, "normal"),command=reset_timer)
reset_button.grid(row=2, column=2)

# Checkmarks
def calc_checkmarks():
    global reps
    return "\u2713" * (reps // 2)
checkmarks = tkinter.Label(text=calc_checkmarks(), bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
checkmarks.grid(row=3, column=1)


window.mainloop()