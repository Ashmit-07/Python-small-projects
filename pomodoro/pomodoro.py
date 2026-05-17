from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS, timer
    if timer is not None:
        window.after_cancel(timer)
        timer = None
    REPS = 0
    canvas.itemconfig(timer_text, text="00:00")
    timerlabel.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")

# ---------------------------- TIMER MECHANISM -------------------------- #
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        countdown(long_break_sec)
        timerlabel.config(text="BREAK", font=(FONT_NAME, 40), fg=RED,
                          bg=YELLOW, highlightthickness=0)
    elif REPS % 2 == 0:
        countdown(short_break_sec)
        timerlabel.config(text="BREAK", font=(FONT_NAME, 40), fg=PINK,
                          bg=YELLOW, highlightthickness=0)
    else:
        countdown(work_sec)
        timerlabel.config(text="WORK", font=(FONT_NAME, 40), fg=GREEN,
                          bg=YELLOW, highlightthickness=0)

# ---------------------------- COUNTDOWN MECHANISM ---------------------- #
def countdown(count):
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(REPS / 2)
        for _ in range(work_session):
            mark += "✓"
        checkmarks.config(text=mark)

# ---------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label
timerlabel = Label(text="Timer", font=(FONT_NAME, 40),
                   fg=GREEN, bg=YELLOW, highlightthickness=0)
timerlabel.grid(row=0, column=1)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file=r"C:\Users\ashmi\OneDrive\Desktop\Programming\Python\small projects medium\pomodoro\tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
timer_text = canvas.create_text(103, 130, text="00:00",
                                fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Buttons
button1 = Button(text="Start", highlightthickness=0, command=start_timer)
button1.grid(row=2, column=0)

button2 = Button(text="Reset", highlightthickness=0, command=reset_timer)
button2.grid(row=2, column=2)

# Checkmarks
checkmarks = Label(text="", fg=GREEN, bg=YELLOW, highlightthickness=0)
checkmarks.grid(row=3, column=1)

window.mainloop()
