from tkinter import *
from quiz_brain import  QuizBrain
THEME_COLOR = "#375362"
FONT_NAME = "Arial"

class QuizInterface():
    def __init__(self,quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        right_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")
        self.window.title("AniQuiz")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_label = Label(text=f"Score: {0}",
                                 font=(FONT_NAME,12,"bold"),
                                 anchor="e",
                                 bg=THEME_COLOR,
                                 fg="White")
        self.score_label.grid(column=2,row=1)
        self.canvas =Canvas(height=250,width=300)
        self.question = self.canvas.create_text(150,125,text="Question",
                                                width = 280,
                                                font=(FONT_NAME,15,"italic"))
        self.canvas.grid(column=1,columnspan=2,row=2,pady=50)
        self.right =Button(image=right_image,width=100,height=97,highlightthickness=0,
                           command=self.clicked_right)
        self.right.grid(row=3,column=1)
        self.wrong = Button(image=wrong_image,width=100,height=97,highlightthickness=0,
                            command=self.clicked_wrong)
        self.wrong.grid(row=3,column=2)
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_text)
        else:
            self.canvas.itemconfig(self.question,text="You have finished the quiz :)")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.right.config(command=self.disable_button)
            self.wrong.config(command=self.disable_button)
            self.canvas.config(bg="white")
    def clicked_right(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def clicked_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(500,self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(500,self.get_next_question)
    def disable_button(self):
        return None