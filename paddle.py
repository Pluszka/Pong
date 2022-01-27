from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, move_line):
        super().__init__()
        self.paddle = self.newPaddle(move_line)

    def newPaddle(self, move_line):
        item = Turtle()
        item.setposition(move_line, y=0)
        item.shape('square')
        item.shapesize(stretch_wid=5, stretch_len=0.5)
        item.penup()
        item.color('white')
        return item

    def move_up(self):
        currentX = self.paddle.xcor()
        currentY = self.paddle.ycor()
        self.paddle.setpos(currentX, currentY+20)

    def move_down(self):
        currentX = self.paddle.xcor()
        currentY = self.paddle.ycor()
        self.paddle.setpos(currentX, currentY - 20)
