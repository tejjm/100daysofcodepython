from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip

FONT_NAME = "Roboto"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    letters_list = [choice(letters) for letter in range(randint(8, 10))]
    password_list+=letters_list

    symbols_list = [choice(symbols) for symbol in range( randint(2, 4))]
    password_list+=symbols_list

    numbers_list = [choice(numbers) for number in range(randint(2, 4))]
    password_list+=numbers_list
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(index=0,string=password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def saving_info():
    website = website_entry.get()
    email_username = email_entry.get()
    password = password_entry.get()
    if len(website) == 0  or len(password) == 0:
        messagebox.showinfo(title="Oops",message=f"You have not entered all the required fields")
    else:
        is_okay = messagebox.askokcancel(title=website,message=f"These are the details entered:\nEmail : {email_username}\nWebsite : {website}\nPassword : {password}")
        if is_okay and len(website) != 0 and len(email_username) !=0:
            with open("passwords.txt","a") as passwords:
                passwords.write(f"[{website}, {email_username}, {password}]\n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas = Canvas(height=200,width=200)
password_image =PhotoImage(file="logo.png")
canvas.create_image(100,100,image=password_image)
canvas.grid(column=2,row=1)

#Website label
website_label = Label(text="Website :",font=(FONT_NAME,8))
website_label.grid(column=1,row=2)
#Email/Username label
email_label = Label(text="Email/Username :",font=(FONT_NAME,8))
email_label.grid(column=1,row=3)
#Password label
password_label = Label(text="Password :",font=(FONT_NAME,8))
password_label.grid(column=1,row=4)
#Generate password button
random_password = Button(text="Generate Password",font=(FONT_NAME,7),width=13,command=generate_password)
random_password.grid(column=3,row=4)
#Add button
add = Button(text="Add",font=(FONT_NAME,7),width=50,command=saving_info)
add.grid(column=2,columnspan=2,row=5)

#Website entry
website_entry = Entry(width=51)
website_entry.focus()
website_entry.grid(column=2,columnspan=2,row=2)
#Email entry
email_entry = Entry(width=51)
email_entry.insert(0,"jobsforuttej@gmail.com")
email_entry.grid(column=2,columnspan=2,row=3)
#Password entry
password_entry = Entry(width=36)
password_entry.grid(column=2,row=4)


window.mainloop()