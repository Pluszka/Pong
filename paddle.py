from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, move_line):
        super().__init__()
        self.newPaddle(move_line)

    def newPaddle(self, move_line):
        self.setposition(move_line, y=0)
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=0.5)
        self.penup()
        self.speed(0)
        self.color('white')
    def move_up(self):
        currentX = self.xcor()
        currentY = self.ycor()
        self.setpos(currentX, currentY+20)

    def move_down(self):
        currentX = self.xcor()
        currentY = self.ycor()
        self.setpos(currentX, currentY - 20)

