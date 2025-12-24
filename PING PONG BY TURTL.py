import turtle
import time

wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=900, height=600)
wn.tracer(0)

def create_paddle(x):
    p = turtle.Turtle()
    p.speed(0)
    p.shape("square")
    p.color("white")
    p.shapesize(stretch_wid=6, stretch_len=1)
    p.penup()
    p.goto(x, 0)
    return p

paddle_left = create_paddle(-420)
paddle_right = create_paddle(420)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx = 5
ball.dy = 5

score_l = 0
score_r = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

def update_score():
    pen.clear()
    pen.write(f"Left: {score_l}    Right: {score_r}",
              align="center", font=("Arial", 18, "normal"))

update_score()

STEP = 30
LIMIT = 250

def move_up(p):
    p.sety(min(p.ycor() + STEP, LIMIT))

def move_down(p):
    p.sety(max(p.ycor() - STEP, -LIMIT))

wn.listen()
# Left paddle → W / S
wn.onkeypress(lambda: move_up(paddle_left), "w")
wn.onkeypress(lambda: move_down(paddle_left), "s")

# Right paddle → Arrow keys
wn.onkeypress(lambda: move_up(paddle_right), "Up")
wn.onkeypress(lambda: move_down(paddle_right), "Down")

while True:
    wn.update()
    time.sleep(1/60)

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if abs(ball.ycor()) > 290:
        ball.dy *= -1

    if ball.xcor() > 440:
        score_l += 1
        update_score()
        ball.goto(0, 0)
        ball.dx = 5
        ball.dy = 5

    if ball.xcor() < -440:
        score_r += 1
        update_score()
        ball.goto(0, 0)
        ball.dx = -5
        ball.dy = 5

    if (390 < ball.xcor() < 420 and
        paddle_right.ycor() - 60 < ball.ycor() < paddle_right.ycor() + 60):
        ball.dx *= -1

    if (-420 < ball.xcor() < -390 and
        paddle_left.ycor() - 60 < ball.ycor() < paddle_left.ycor() + 60):
        ball.dx *= -1
