#simple ping pong game in Python3 

import turtle
import winsound

wn =  turtle.Screen()
wn.title("Pong by Billy Lin")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score variables
score_1 =0
score_2 =0

#paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("green")
paddle_1.shapesize(stretch_wid=5,stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350,0)

#paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("red")
paddle_2.shapesize(stretch_wid=5,stretch_len=1)
paddle_2.penup()
paddle_2.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("blue")

ball.penup()
ball.goto(0,0)

ball.dx = 0.5
ball.dy = -0.5

#Pen for ScoreBoard
pen =  turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0   Player 2: 0", align = "center", font= ("Comic Sans", 24,  "normal"))

#Functions for moving paddles
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

def paddle_1_right():
    x = paddle_1.xcor()
    x += 20
    paddle_1.setx(x)

def paddle_1_left():
    x = paddle_1.xcor()
    x -= 20
    paddle_1.setx(x)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

def paddle_2_right():
    x = paddle_2.xcor()
    x += 20
    paddle_2.setx(x)

def paddle_2_left():
    x = paddle_2.xcor()
    x -= 20
    paddle_2.setx(x)

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "s")
#wn.onkeypress(paddle_1_left, "a")
#wn.onkeypress(paddle_1_right, "d")
wn.onkeypress(paddle_2_up, "Up")
wn.onkeypress(paddle_2_down, "Down")
#wn.onkeypress(paddle_2_left, "Left")
#wn.onkeypress(paddle_2_right, "Right")


#main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0 )
        ball.dx *= -1
        score_1 +=1
        pen.clear()
        pen.write("Player 1: {}   Player 2: {}".format(score_1, score_2), align = "center", font= ("Comic Sans", 24,  "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0 )
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}   Player 2: {}".format(score_1, score_2), align = "center", font= ("Comic Sans", 24,  "normal"))

    #Paddle and Ball Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)