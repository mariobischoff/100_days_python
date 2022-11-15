from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some question text", fill=THEME_COLOR, font=QUESTION_FONT, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.true_img = PhotoImage(file="img/true.png")
        self.button_true = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(column=0, row=2, padx=20, pady=20)

        self.false_img = PhotoImage(file="img/false.png")
        self.button_false = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_quesquion()

        self.window.mainloop()

    def get_next_quesquion(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You're reached the end.")
            self.button_true.config(state=DISABLED)
            self.button_false.config(state=DISABLED)

    
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_quesquion)