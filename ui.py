from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizGui:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("PahlawanJoey's QuizGame")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=350, height=300, bg="white")
        self.quiz_text = self.canvas.create_text((175, 150), width=285, text="question_text", fill=THEME_COLOR,
                                                 font=("Arial", 20, "bold"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.true_button_img = PhotoImage(file="./images/true.png")
        self.false_button_img = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=self.true_button_img, highlightthickness=0, bd=0, command=self.question_true)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=self.false_button_img, highlightthickness=0, bd=0, command=self.question_false)
        self.false_button.grid(column=1, row=2)
        self.score_text = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score_text.grid(column=1, row=0)
        self.question_text()
        self.window.mainloop()

    def update_score(self):
        self.score_text.config(text=f"Score: {self.quiz.score}")

    def question_text(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def question_true(self):
        self.feedback(self.quiz.check_answer("True"))

    def question_false(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.update()
        self.window.after(1000, func=self.question_text())
        self.update_score()
