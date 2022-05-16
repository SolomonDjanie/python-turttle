import turtle, random


turtle.colormode(1)

win = turtle.Screen()

win.bgcolor(0 ,0 ,0)

turtle.speed(0)

turtle.width(1)

for k in range (10):
     turtle.color(random.uniform (0 , 1),random.uniform (0 , 1),random.uniform (0 , 1))

     turtle.circle(k*1.5)
