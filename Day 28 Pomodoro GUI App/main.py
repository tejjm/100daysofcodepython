from tkinter import *
import math
import winsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = ""
reps = 0
time = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps,time,CHECK_MARK
    reps = 0
    window.after_cancel(time)
    timer.config(text="Timer")
    canvas.itemconfig(timer_text,text=f"00:00")
    CHECK_MARK=""

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps,CHECK_MARK
    reps+=1
    if reps in (1,3,5,7):
        count_down(WORK_MIN*60)
        timer.config(text="Work",fg=GREEN)
    elif reps == 8:
        count_down(LONG_BREAK_MIN*60)
        timer.config(text="Break",fg=RED)
    elif reps in (2,4,6):
        count_down(SHORT_BREAK_MIN*60)
        timer.config(text="Break",fg=PINK)
        CHECK_MARK+="✓"
        checkmark.config(fg=GREEN, bg=YELLOW,text=CHECK_MARK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global time
    count_min =  math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}" #Dynamic typing which is only available in python
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        time = window.after(1000,count_down,count-1)
    if count == 0:
        start_timer()
        winsound.Beep(1000,500)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)
#Timer Label
timer = Label(text="Timer",font=(FONT_NAME,40))
timer.config(fg=GREEN,bg=YELLOW)
timer.grid(column=2,row=1)

# Check Mark Label
checkmark = Label(text="",font=(FONT_NAME,8))
checkmark.config(fg=GREEN,bg=YELLOW,text=CHECK_MARK)
checkmark.grid(column=2,row=4)
#Start button
start_button = Button(text="Start",font=(FONT_NAME,8),command=start_timer)
start_button.grid(column=1,row=3)

#Reset button
reset_button = Button(text="Reset",font=(FONT_NAME,8),command=reset_timer)
reset_button.grid(column=3,row=3)

window.mainloop()