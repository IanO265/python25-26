import turtle
bob=turtle.Turtle()

def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()


def polygon(sides, dist, color):
  bob.color(color)
  angle = 360/sides
  bob.fillcolor(color)
  bob.begin_fill()
  for times in range(sides):        
    bob.forward(dist)
    bob.left(angle)
    bob.end_fill()


def stair(disatnce, color, angle, amount):
    bob.color(color)
    for times in range(amount):
        bob.forward(disatnce)
        bob.left(angle)
        bob.forward(disatnce)
        bob.right(angle)


def spiral(disatnce, color, angle, times):
    for times in range(10):
        bob.comet(disatnce, color, angle, times)
        bob.goto(20,50)


def comet(distance, angle, color, times):
  bob.color(color)
  for times in range(10):
    bob.width(times)
    bob.forward(distance)
    bob.left(angle)

def star(distance,color,width):
  bob.color(color)
  bob.width(width)
  for times in range(10):
    bob.forward(distance)
    bob.left(135)
    

