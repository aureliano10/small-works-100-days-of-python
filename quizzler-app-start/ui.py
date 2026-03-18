from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx= 20, pady= 20, background=THEME_COLOR)

        self.score_label = Label(text= f"Score: {self.quiz.score}", fg= "white", bg= THEME_COLOR)
        self.score_label.grid(row=0, column=1, pady= 50)

        self.canvas = Canvas(width= 300, height= 250, bg= "white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width= 280,
                                                     text="question text",
                                                     fill=THEME_COLOR ,
                                                     font=("Arial", 20, "italic")
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2)

        true_img = PhotoImage(file= "images/true.png")
        self.button_true = Button(image= true_img, highlightthickness= 0, command= self.true_question_button)
        self.button_true.grid(row=2, column= 0, pady= 50)


        false_img = PhotoImage(file= "images/false.png")
        self.button_false = Button(image= false_img, highlightthickness= 0, command= self.false_question_button)
        self.button_false.grid(row=2, column= 1, pady= 50)

        self.get_next_cuestion()

        self.window.mainloop()

    def get_next_cuestion(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= f"You end this quiz\n"
                                                             f"Your final score is: {self.quiz.score}")
            self.button_true.config(state= "disabled")
            self.button_false.config(state= "disabled")


    def true_question_button(self):
        self.update_score(self.quiz.check_answer("True"))

    def false_question_button(self):
        self.update_score(self.quiz.check_answer("False"))

    def update_score(self, answer):
        if answer:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_cuestion)





