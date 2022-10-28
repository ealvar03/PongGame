from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed_ball = 0.1

    def move_ball(self):
        ycor = self.ycor() + self.y_move
        xcor = self.xcor() + self.x_move
        self.goto(xcor, ycor)

    def bounce_ycor(self):
        self.y_move *= -1

    def bounce_xcor(self):
        self.x_move *= -1
        self.speed_ball *= 0.9

    def new_ball(self):
        self.goto(0, 0)
        self.speed_ball = 0.1
        self.bounce_xcor()





