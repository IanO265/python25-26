from myFunctions import *
from random import *

bob.speed(0)

star(100,"purple",4)
turtle.colormode(255)
turtle.bgcolor("black")
turtle.tracer(False)


#wires
bob.penup()
bob.goto(-900,450)
bob.pendown()
bob.color("grey")
bob.left(90)
for times in range(30):
    bob.forward(1800)
    bob.left(181)
    bob.forward(1800)
    bob.right(181)


#checkered stars
for times in range(90):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    c =(r,g,b)

    fill=(r,g,b)
    x = randint(-500,500)
    y = randint(-400,400)
    jump(x,y)

    
    bob.begin_fill()
    star(100,c,2)
    bob.fillcolor(c)
    bob.end_fill()


#strings    
bob.penup()
bob.goto(-900,450)
bob.pendown()
bob.color("white")
bob.left(91)
for times in range(80):
    bob.right(181)
    bob.forward(1800)
    bob.left(181)
    bob.forward(1800)
