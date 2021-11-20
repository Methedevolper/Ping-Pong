import turtle

a_wins = False
b_wins = False
c_wins = False

# Set up the screen
turtle.Screen()
wn = turtle.Screen()
wn.title("Ping Pong game by Mohamed")
wn.bgcolor("orange")
wn.setup(width=1366, height=768)
wn.tracer(0)

# Score
score_a = 0
score_b = 0
score_c = 0
score_lim = 12
switch = True

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(2000)
paddle_a.color("green")
paddle_a.shape("circle")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(200)
paddle_b.color("blue")
paddle_b.shape("circle")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# Paddle C
paddle_c = turtle.Turtle()
paddle_c.speed(200)
paddle_c.color("blue")
paddle_c.shape("circle")
paddle_c.penup()
paddle_c.goto(350, 0)
paddle_c.shapesize(stretch_wid=5, stretch_len=1)

paddle_a_speed = 50
paddle_b_speed = 50
paddle_c_speed = 50
paddle_d_speed = 50

# Ball
ball = turtle.Turtle()
ball.speed(200)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dy = 0.4
ball.dx = 0.4

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("purple")
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("bevan", 50, "normal"))

# Win
win = turtle.Turtle()
win.speed(20000)
win.penup()
win.color("purple")
win.hideturtle()
win.goto(0, 0)


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += paddle_a_speed
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= paddle_a_speed
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += paddle_b_speed
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= paddle_b_speed
    paddle_b.sety(y)


def paddle_c_up():
    y = paddle_c.ycor()
    y += paddle_c_speed
    paddle_a.sety(y)


def paddle_c_down():
    y = paddle_c.ycor()
    y -= paddle_c_speed
    paddle_c.sety(y)


# Control


turtle.listen()
turtle.onkey(paddle_a_up, "w")
turtle.onkey(paddle_a_down, "s")

turtle.onkey(paddle_b_up, "Up")
turtle.onkey(paddle_b_down, "Down")

turtle.onkey(paddle_c_down, "Right")
turtle.onkey(paddle_c_up, "Left")
# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    elif ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1

    # Paddle
    if -340 < ball.xcor() < 350 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1
    if -340 > ball.xcor() > -350 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
    if -340 > ball.xcor() > 350 and paddle_c.ycor() + 50 > ball.ycor() > paddle_c.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1

    pen.clear()
    pen.write(f"Player A: {score_a}  Player B: {score_b}  Player C: {score_c}", align="center",
              font=("bevan", 24, "normal"))

    if score_a == score_lim:
        turtle.clearscreen()
        a_wins = True
        break

    elif score_b == score_lim:
        turtle.clearscreen()
        b_wins = True
        break

    elif score_c == score_lim:
        turtle.clearscreen()
        c_wins = True
        break

while True:
    if a_wins:
        wn.bgcolor("black")
        win.write("Player A wins", align="center", font=("bevan", 50, "normal"))
    elif b_wins:
        wn.bgcolor("black")
        win.write("Player B wins", align="center", font=("bevan", 50, "normal"))
    elif c_wins:
        wn.bgcolor("black")
        win.write("player C wins", align="center", font=("bevan", 50, "normal"))
