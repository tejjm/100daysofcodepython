class QuizBrain():
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.turn = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        answer = input(f"Q.no.{self.question_number} {current_question.text}. (True/False)? :\n")
        self.check_answer(answer,current_question.answer)
    # def total_score(self):
    #     print("You have completed the quiz!")
    #     user_score = self.score
    #     total = len(self.question_list)
    #     print(f'Your total score is {user_score}/{total}!"')

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score+=1
            self.turn+=1
        else:
            print("You got it wrong!")
            self.turn += 1
        print(f"The correct answer is {correct_answer}")
        if self.still_has_questions() is not True:
            print('\n')
            print("You have completed the quiz!")

        print(f"Your total score is {self.score}/{self.turn} !")
        print('\n')
