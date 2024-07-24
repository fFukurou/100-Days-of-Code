from tkinter import * #type: ignore
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        right_btn_img = PhotoImage(file="Day-34-Quizzler/quizzler/images/true.png")
        wrong_btn_img = PhotoImage(file="Day-34-Quizzler/quizzler/images/false.png")
        self.question_text = self.canvas.create_text(150, 125, font=("Arial", 14, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.right_button = Button(image=right_btn_img, highlightthickness=0, command=self.press_right_button)
        self.right_button.grid(row=2,column=0)

        self.wrong_button = Button(image=wrong_btn_img, highlightthickness=0, command=self.press_wrong_button)
        self.wrong_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.right_button.config(state="active")
        self.wrong_button.config(state="active")
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_txt = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_txt)

        else:
            self.canvas.itemconfig(self.question_text, text= "You have reached the end of the quiz!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")


    def press_right_button(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.right_button.config(state="disabled")
        self.wrong_button.config(state="disabled")

    def press_wrong_button(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.right_button.config(state="disabled")
        self.wrong_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right is True:
            self.canvas.config(bg="green")
        elif is_right is False:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
        
