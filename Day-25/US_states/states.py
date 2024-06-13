import turtle

class States(turtle.Turtle):
    def __init__(self, name, x, y) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(name)