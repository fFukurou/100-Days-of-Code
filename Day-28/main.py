#Pomodoro Project

from tkinter import * #type: ignore
import math
# ---------------------------- CONSTANTS ------------------------------- #
DEEP_BLUE = "#17153B"
NAVY = "#2E236C"
BLUE = "#433D8B"
PINKISH = "#C8ACD6"
GREEN = "#32CD32"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
cycles = 0
timer = None



def start_pomodoro():
    reset_timer()
    start_timer()
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    global cycles
    if timer != None:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    check_mark.config(text="")
    pomodoro.config(text="")
    reps = 0
    cycles = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global cycles
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_seconds)
        label_timer.config(text="LONG BREAK", fg=PINKISH)
        reps = 0
        cycles += 1

    elif reps % 2 == 0:
        countdown(short_break_seconds)
        label_timer.config(text="SHORT BREAK", fg=PINKISH)

    else:
        countdown(work_seconds)
        label_timer.config(text="WORK", fg=PINKISH)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    global reps

    count_minute = math.floor(count / 60)
    count_second = count % 60   

    if count_minute < 10:
        count_minute = f"0{count_minute}"

    if count_second < 10:
        count_second = f"0{count_second}"


    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)

    else:
        start_timer()
        if reps % 2 == 0:
            check_mark.config(text="✔"  * int(reps/2), font=(FONT_NAME, 15))
        if reps % 8 == 0:
            pomodoro.config(text="🍑"  * cycles, font=(FONT_NAME, 15))



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=DEEP_BLUE)


canvas = Canvas(width=200, height=223, bg=DEEP_BLUE, highlightthickness=0)
tomato_img = PhotoImage(file="Day-28/tomato.png")
canvas.create_image(100, 110, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label_timer = Label(text="Timer", font=(FONT_NAME, 32, "bold", ), bg=DEEP_BLUE, fg=PINKISH)
label_timer.grid(row=0, column= 1)



start_button = Button(text="Start", command=start_pomodoro, bg=NAVY, fg=PINKISH)
start_button.grid(row=3, column=0)

reset_button = Button(text="Reset", command=reset_timer, bg=NAVY, fg=PINKISH)
reset_button.grid(row=3, column=2)

check_mark = Label(bg=DEEP_BLUE, fg=GREEN)
check_mark.grid(row=4, column= 1)

pomodoro = Label(bg=DEEP_BLUE, fg=PINKISH)
pomodoro.grid(row=5, column= 1)

window.mainloop()