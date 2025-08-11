from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
#Creating a question bank
question_bank = []
for entry in question_data:
    q = Question(entry['question'], entry['correct_answer'])
    question_bank.append(q)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
