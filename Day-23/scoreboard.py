from turtle import Turtle


FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    current_level = 0
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-260, 250)
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {Scoreboard.current_level + 1}", align='left', font=FONT)
        

    def increase_level(self):
        Scoreboard.current_level += 1
        self.update_scoreboard()
