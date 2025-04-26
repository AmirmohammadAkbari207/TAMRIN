import turtle
import math


screen = turtle.Screen()
screen.bgcolor("white")


gun = turtle.Turtle()
gun.shape("square")
gun.color("black")
gun.shapesize(stretch_wid=0.5, stretch_len=2)
gun.penup()
gun.goto(-200, -100)


human = turtle.Turtle()
human.penup()
human.goto(100, 0)
human.pendown()


human.circle(10)


human.goto(100, -40)


human.goto(85, -20)
human.penup()
human.goto(100, -40)
human.pendown()
human.goto(115, -20)


human.penup()
human.goto(100, -40)
human.pendown()
human.goto(85, -60)
human.penup()
human.goto(100, -40)
human.pendown()
human.goto(115, -60)


ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(-200, -100)


speed = float(input("🔫 سرعت شلیک توپ را وارد کنید (مثلاً 15): "))
angle = float(input("🎯 زاویه شلیک توپ را وارد کنید (مثلاً 45): "))


vx = speed * math.cos(math.radians(angle))
vy = speed * math.sin(math.radians(angle))
gravity = 0.5


while ball.ycor() >= -100:
    ball.setx(ball.xcor() + vx)
    ball.sety(ball.ycor() + vy)
    vy -= gravity  

    
    if abs(ball.xcor() - 100) < 10 and abs(ball.ycor() - 0) < 10:
        human.color("red")  
        print("🎯 برخورد انجام شد!")
        break

turtle.done()
