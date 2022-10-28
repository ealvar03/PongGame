from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Arcade Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

if __name__ == '__main__':
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        ball.move_ball()

        # Detect collision with top and bottom walls and bounce the ball
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_ycor()

        # Detect collision with paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < 320:
            ball.bounce_xcor()

        # Right paddle misses a ball
        if ball.xcor() > 390:
            ball.new_ball()
            score.add_left_score()

        # Left paddle misses a ball
        if ball.xcor() < -390:
            ball.new_ball()
            score.add_right_score()

    screen.exitonclick()
