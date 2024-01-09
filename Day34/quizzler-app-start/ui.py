from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface(Tk):
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        super().__init__()
        self.title("Quizzler")
        true_button_image = PhotoImage(file="./images/true.png")
        false_button_image = PhotoImage(file="./images/false.png")

        self.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text="Score: 0", font=("Arial", 12, "bold"), bg=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300, bg="White", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Text",
            font=("Arial", 20, "italic"))
        self.true_button = Button(image=true_button_image, command=self.true_pressed, highlightthickness=0)
        self.false_button = Button(image=false_button_image, command=self.false_pressed, highlightthickness=0)

        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)
        self.score.grid(column=1, row=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.get_next_question()

        self.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score.config(text=" ")
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.        Your score is: "
                                                            f"{self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
            self.score.config(text=f"Score: {self.quiz.score}")
            self.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="Red")
            self.after(1000, self.get_next_question)
