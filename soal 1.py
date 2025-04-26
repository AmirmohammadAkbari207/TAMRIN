import turtle
import math

def draw_polygon(sides, length):
    """ رسم یک n-ضلعی منتظم """
    angle = 360 / sides
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(angle)

def draw_tangent_polygons(sides, length):
    """ رسم یک n-ضلعی و سپس n عدد n-ضلعی مماس بر هر ضلع آن """
    angle = 360 / sides

   
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-length / 2, 0)
    turtle.pendown()
    draw_polygon(sides, length)

   
    for _ in range(sides):
        turtle.penup()
        turtle.forward(length)  
        turtle.pendown()
        draw_polygon(sides, length) 
        turtle.left(angle) 


sides = int(input("تعداد اضلاع را وارد کنید (بزرگتر از 2): "))
length = 100 


draw_tangent_polygons(sides, length)
turtle.done()
