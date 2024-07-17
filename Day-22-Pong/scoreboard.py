from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.draw_dashed_line()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=("Courier", 55, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=("Courier", 55, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def draw_dashed_line(self):
        self.goto(0, -300)
        self.setheading(90)
        for _ in range(15):
            self.pendown()
            self.forward(200)
            self.penup()
            self.forward(10)
            self.penup()