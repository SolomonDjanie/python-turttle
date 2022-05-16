import turtle, random

turtle.colormode(1)

win = turtle.Screen()

win.bgcolor(0 ,0 ,0)

turtle.speed(0)

turtle.width(1)

for k in range (50):
     turtle.color(random.uniform (0 , 1),random.uniform (0 , 1),random.uniform (0 , 1))
     turtle.dot(k*3.5)
     turtle.up()
     
     turtle.fd(50)
     turtle.bk(100)
     turtle.lt(160)
     turtle.fd(100)
     turtle.bk(20)

     turtle.rt(90)
     
     


 
