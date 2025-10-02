# BACKGROUND_COLOR = "#B1DDC6"
# current_romaji = ""
# from tkinter import *
# import pandas as pd
# import random
# # ---------------------------- Reading Data and Flash Card Functionality ------------------------------- #
# hiragana = pd.read_csv("./data/Hiragana.csv")
# def pick_hira():
#     global current_romaji,flip_timer
#     window.after_cancel(flip_timer)
#     canvas.itemconfig(canvas_image,image=front_card)
#     canvas.itemconfig(heading,text = "Japanese",fill="black")
#     random_num = random.randint(0,45)
#     random_hira = hiragana.at[random_num,"Character"]
#     canvas.itemconfig(character,text=random_hira,fill="black")
#     romaji = hiragana.at[random_num,"Romaji"]
#     current_romaji = romaji
#     canvas.itemconfig(character,text=random_hira)
#     canvas.itemconfig(heading,text = "Japanese")
#     flip_timer = window.after(3000,flip_card)
#
# def flip_card():
#     global  current_romaji
#     canvas.itemconfig(canvas_image,image=back_card)
#     canvas.itemconfig(character,text=current_romaji,fill="white")
#     canvas.itemconfig(heading,text = "English",fill="white")
# # ---------------------------- UI SETUP ------------------------------- #
#
# window = Tk()
# window.title("HiraFlash")
# window.config(bg=BACKGROUND_COLOR,pady=10,padx=10)
# canvas = Canvas(width=800,height=550,bg=BACKGROUND_COLOR,highlightthickness=0)
# front_card = PhotoImage(file="./images/card_front.png")
# back_card = PhotoImage(file="./images/card_back.png")
# canvas_image = canvas.create_image(410,280,image=front_card)
# canvas.grid(row=1,column=1,columnspan=2)
# #Buttons
# right_image =  PhotoImage(file="./images/right.png")
# right = Button(image=right_image,bg=BACKGROUND_COLOR,highlightthickness=0,width=100,height=100,relief="flat",command=pick_hira)
# right.grid(row=2,column=1)
#
# wrong_image =  PhotoImage(file="./images/wrong.png")
# wrong = Button(image=wrong_image,bg=BACKGROUND_COLOR,highlightthickness=0,width=100,height=100,relief="flat",command=pick_hira)
# wrong.grid(row=2,column=2)
#
# #Text
# character = canvas.create_text(410, 263, text="Ready?", font=("Meiryo", 60, "bold"))
# heading = canvas.create_text(410, 150, text="Japanese", font=("Meiryo", 20))
# flip_timer = window.after(3000,flip_card)
#
# pick_hira()
#
#
# window.mainloop()
