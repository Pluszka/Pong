from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Rockwell", 25, 'bold')


class Score(Turtle):

    def __init__(self, side, col):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setposition(x=0, y=-300)
        self.draw()
        self.color(col)
        self.goto(y=250, x=side)
        self.prompt()

    def prompt(self):
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def updateScore(self):
        self.score += 1
        self.clear()
        self.prompt()

    def draw(self):
        self.setheading(90)
        self.color('#1F7A8C')
        for _ in range(10):
            self.forward(30)
            self.pendown()
            self.forward(30)
            self.penup()