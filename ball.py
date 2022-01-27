from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball = self.create()



    def create(self):
        new = Turtle()
        new.shape('square')
        new.penup()
        new.color('white')
        new.shapesize(stretch_wid=0.5, stretch_len=0.5)
        return new