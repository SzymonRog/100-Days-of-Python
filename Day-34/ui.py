from tkinter import *

THEME_COLOR = "#375362"
class UI:
    def __init__(self, quiz_brain):
        self.QuizBrain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=400, height=300, bg="white")
        self.question_text = self.canvas.create_text(200, 150, text="Question Text", width=250, font=("Arial", 20, "italic"),)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=30, padx=30)

        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")

        self.correct_button = Button(text="Correct", image=self.true_img, highlightthickness=0, command=self.true_clicked)
        self.correct_button.grid(row=2, column=0)

        self.wrong_button = Button(text="Wrong", image=self.false_img, highlightthickness=0, command=self.false_clicked)
        self.wrong_button.grid(row=2, column=1)

        self.score_label = Label(text="Score: 0", font=("Arial", 15, "bold"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)


    def disable_buttons(self):
        self.correct_button.config(state="disabled")
        self.wrong_button.config(state="disabled")

    def print_question(self, question):
        self.canvas.itemconfig(self.question_text, text=question.text)

    def true_clicked(self):
        self.QuizBrain.check_answer("True", self.canvas, self.score_label)
        self.window.after(1000, self.QuizBrain.next_question, self.print_question, self.canvas, self.disable_buttons)

    def false_clicked(self):
        self.QuizBrain.check_answer("False", self.canvas, self.score_label)
        self.window.after(1000, self.QuizBrain.next_question, self.print_question, self.canvas, self.disable_buttons)





