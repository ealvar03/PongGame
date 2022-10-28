from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.goto(position)
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()

    def move_up(self):
        self.sety(self.ycor() + 20)

    def move_down(self):
        self.sety(self.ycor() - 20)
