from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Rockwell", 25, 'bold')

class Score(Turtle):

    def __init__(self, side):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(y=250, x=side)
        self.prompt()

    def prompt(self):
        self.write(self.score, align=ALIGNMENT, font=FONT)

