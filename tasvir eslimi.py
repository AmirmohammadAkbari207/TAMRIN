import turtle
import math


screen = turtle.Screen()
screen.bgcolor("white")


pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.width(2)


def draw_islamic_pattern(radius, angle, step):
    for _ in range(int(360 / step)):
        pen.circle(radius, angle)
        pen.left(step)


pen.penup()
pen.goto(-50, 0)
pen.pendown()
draw_islamic_pattern(50, 60, 10)

pen.penup()
pen.goto(50, 0)
pen.pendown()
draw_islamic_pattern(50, 60, 10)

pen.penup()
pen.goto(0, -50)
pen.pendown()
draw_islamic_pattern(50, 60, 10)

pen.penup()
pen.goto(0, 50)
pen.pendown()
draw_islamic_pattern(50, 60, 10)


for angle in range(0, 360, 45):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.setheading(angle)
    pen.forward(100)


screen.mainloop()
