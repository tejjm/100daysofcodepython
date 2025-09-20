from tkinter import *

#Button
def Km_to_Miles():
    km = round(float(entry.get())*0.6213712,2)
    entered = str(km)
    label2_2.config(text = entered)

window = Tk()
window.title("Km to Mile")
window.minsize(width=250,height=100)

#Label
label1_2 = Label(text="is equal to",font=("Arial",10,"bold"),)
label1_2.grid(column=1,row=2)

label2_2 = Label(text= "0",font=("Arial",10,"bold"),)
label2_2.grid(column=2,row=2)

label3_2 = Label(text= "Miles",font=("Arial",10,"bold"),)
label3_2.grid(column=3,row=2)

label3_1 = Label(text= "Kms",font=("Arial",10,"bold"),)
label3_1.grid(column=3,row=1)

button = Button(text="Calculate",command=Km_to_Miles)
button.grid(column=2,row=3)
#Entry
entry = Entry(width=20)
entry.insert(END,string="0")
entry.grid(column=2,row=1)



window.mainloop()
