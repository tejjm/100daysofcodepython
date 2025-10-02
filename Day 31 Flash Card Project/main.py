BACKGROUND_COLOR = "#B1DDC6"
random_index = 0
current_romaji = ""
random_kana = ""
known_kana = []
max_index = 45
from tkinter import *
import pandas as pd
import random
import json
# ---------------------------- Reading Data and Flash Card Functionality ------------------------------- #
data = pd.read_csv("./data/Hiragana_Katakana_Combined.csv")
json_str = data.to_json(orient="records",force_ascii=False)
json_data = json.loads(json_str)
with open("all_kana.json","w",encoding="utf-8") as f:
    json.dump(json_data,f,indent=4,ensure_ascii=False)
random_index = random.randint(0,45)
with open("All_Kana.json","r",encoding="utf-8") as file:
    kana = json.load(file)
def pick_card():
    global random_index,current_romaji,random_kana,flip_timer
    window.after_cancel(flip_timer)
    try:
        if len(kana) <= 0:
            practice_complete()
        canvas.itemconfig(canvas_image,image=front_card)
        random_index = random.randint(0, max_index)
        random_kana = kana[random_index]["Character"]
        current_romaji = kana[random_index]["Romaji"]
        canvas.itemconfig(character,text=random_kana,fill="black")
        canvas.itemconfig(heading,text = "Kana",fill="black")
        flip_timer = window.after(3000, flip_card)
    except:
        practice_complete()


def flip_card():
    global  current_romaji
    try:
        canvas.itemconfig(canvas_image,image=back_card)
        canvas.itemconfig(character,text=current_romaji,fill="white")
        canvas.itemconfig(heading,text = "English",fill="white")
    except:
        practice_complete()
def eject_to_known():
    global max_index
    try:
        ejected_item = kana.pop(random_index)
        max_index-=1
        print(len(kana))
        known_kana.append((ejected_item))
    except:
        practice_complete()

def practice_complete():
    canvas.itemconfig(canvas_image,image=front_card)
    canvas.itemconfig(character,text="Good job!",fill="black")
    canvas.itemconfig(heading,text = "You have finished practicing all 46 KANA",fill="black")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("KanaFlash")
window.config(bg=BACKGROUND_COLOR,pady=10,padx=10)
canvas = Canvas(width=800,height=550,bg=BACKGROUND_COLOR,highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(410,280,image=front_card)
canvas.grid(row=1,column=1,columnspan=2)
#Buttons
right_image =  PhotoImage(file="./images/right.png")
right = Button(image=right_image,bg=BACKGROUND_COLOR,highlightthickness=0,width=100,height=100,relief="flat",command=lambda:[pick_card(),eject_to_known()])
right.grid(row=2,column=1)

wrong_image =  PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrong_image,bg=BACKGROUND_COLOR,highlightthickness=0,width=100,height=100,relief="flat",command=pick_card)
wrong.grid(row=2,column=2)

# Text

character = canvas.create_text(410, 263, text="Ready", font=("Meiryo", 60, "bold"))
heading = canvas.create_text(410, 150, text="Kana", font=("Meiryo", 20,"bold"))
flip_timer = window.after(3000, flip_card)
pick_card()

window.mainloop()
