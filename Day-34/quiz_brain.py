from tkinter.messagebox import QUESTION

import question_model
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.end_of_game_question = question_model.Question("End of Game", "")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self, print_question, canvas, disable_buttons=None):
        canvas.config(bg="white")
        if self.still_has_questions():
            self.current_question = self.question_list[self.question_number]
            print_question(self.current_question)
            self.question_number += 1
        else:
            print_question(self.end_of_game_question)
            if disable_buttons:  # <- dodane
                disable_buttons()



    def check_answer(self, user_answer,canvas, score_label):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            canvas.config(bg="green")
        else:
            canvas.config(bg="red")

        score_label.config(text=f"Score: {self.score}")

        return 1
