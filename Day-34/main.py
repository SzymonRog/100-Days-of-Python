from question_model import Question
from data import *
from quiz_brain import QuizBrain
from ui import UI
import html

question_bank = []

for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)



quiz = QuizBrain(question_bank)
ui = UI(quiz_brain=quiz)



quiz.next_question(ui.print_question, ui.canvas)



ui.window.mainloop()




