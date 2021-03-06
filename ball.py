from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def create(self):
        self.shape('square')
        self.penup()
        self.color('#1F7A8C')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def change(self, col):
        self.color(col)