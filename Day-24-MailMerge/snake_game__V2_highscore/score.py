from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 13, 'normal')




class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("Day-24-MailMerge/snake_game__V2_highscore/data.txt", 'r') as file:
            self.highscore = int(file.read())

        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.refresh()


    def refresh(self):
        self.clear()
        self.write(f"Score:   {self.score} High Score: {self.highscore} ", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        with open("Day-24-MailMerge/snake_game__V2_highscore/data.txt", 'w') as file:
            file.write(f"{self.score}")
        self.refresh()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score 
        self.score = 0
        self.refresh()






"""     def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT) """