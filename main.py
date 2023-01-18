import turtle
import random


def col():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    colr= (r, g, b)
    return colr


turtle.colormode(255)
timturtle = turtle.Turtle()

turtle.Screen().canvheight = 300
turtle.Screen().canvwidth = 300
timturtle.speed("fastest")
timturtle.hideturtle()
timturtle.penup()
ycor=0
for i in range(10):
    timturtle.setposition(-200,-200+ycor)
    for j in range(10):
        timturtle.dot(20,col())
        timturtle.fd(40)
    ycor+=40

turtle.Screen().exitonclick()