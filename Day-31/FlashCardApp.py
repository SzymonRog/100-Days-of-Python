import random
import os
import pandas as pd
import tkinter as tk

class FlashCardApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Flash Card App")
        self.root.config(padx=20,pady=20,bg="#B1DDC6")


        if os.path.exists("data/words_to_learn.csv"):
            self.data = pd.read_csv("data/words_to_learn.csv")
        else:
            self.data = pd.read_csv("data/french_words.csv")

        self.word_dict = self.data.to_dict(orient="records")
        self.word_card = {}

        self.front_img = tk.PhotoImage(file="./images/card_front.png")
        self.back_img = tk.PhotoImage(file="./images/card_back.png")

        self.canvas = tk.Canvas(width=900, height=550, bg="#B1DDC6", highlightthickness=0)
        self.image_id = self.canvas.create_image(450, 275, image=self.front_img)
        self.language_text = self.canvas.create_text(450, 150, font=("Ariel", 32, "italic"))
        self.word_text = self.canvas.create_text(450, 275, font=("Ariel", 52, "italic"))
        self.canvas.grid(column=0, row=0, columnspan=3)

        self.check_img = tk.PhotoImage(file="./images/right.png")
        self.check_button = tk.Button(image=self.check_img, highlightthickness=0, relief="flat", bd=0, command=self.right)
        self.check_button.grid(column=2, row=1)

        self.wrong_img = tk.PhotoImage(file="./images/wrong.png")
        self.wrong_button = tk.Button(image=self.wrong_img, highlightthickness=0, relief="flat", bd=0, command=self.wrong)
        self.wrong_button.grid(column=0, row=1)

        self.exit_button = tk.Button(text="Exit", width=7, highlightthickness=0, relief="flat", bd=0, command=self.root.destroy,font=("Ariel", 20, "bold"))
        self.exit_button.grid(column=1, row=1)


        self.right_answer = 0
        self.wrong_answer = 0

        self.score_label = tk.Label(text=f"Score: {self.right_answer}/{self.right_answer + self.wrong_answer}", font=("Ariel", 15, "bold"), bg="#B1DDC6")
        self.score_label.grid(column=1, row=3)

        self.update_game()

    def choose_word(self):
        return random.choice(self.word_dict)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.right_answer}/{self.right_answer + self.wrong_answer}")

    def set_card(self, language="French"):
        self.canvas.itemconfig(self.language_text, text=language)
        self.canvas.itemconfig(self.word_text, text=self.word_card.get(language, ""))
        image = self.front_img if language == "French" else self.back_img
        self.canvas.itemconfig(self.image_id, image=image)

    def update_game(self):
        self.update_score()
        self.word_card = self.choose_word()
        self.set_card()
        self.root.after(3000, self.set_card, "English")

    def right(self):
        self.right_answer += 1
        self.update_word_list()
        self.update_game()

    def wrong(self):
        self.wrong_answer += 1
        self.update_game()

    def update_word_list(self):
        new_df = pd.read_csv("data/words_to_learn.csv")
        new_df = new_df[new_df.French != self.word_card["French"]]
        new_df.to_csv("data/words_to_learn.csv", index=False)


