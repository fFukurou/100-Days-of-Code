from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 13, 'normal')




class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.refresh()


    def refresh(self):
        self.clear()
        self.write(f"Score:   {self.score}", move=False, align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)