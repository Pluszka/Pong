from turtle import Turtle

move_line = 375

class Paddle:

    def __init__(self):
        super().__init__()
        self.paddle = self.newPaddle()

    def newPaddle(self):
        item = Turtle()
        item.setposition(move_line, y=40)
        item.shape('square')
        item.shapesize(stretch_wid=5, stretch_len=1)
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
