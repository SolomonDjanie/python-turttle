import turtle
import random




t = turtle.Turtle()


win = turtle.Screen()


win.bgcolor('blue')
win.title('Using turtle tracer method')
win.setup(width = 800, height = 500)


turtle.colormode(255)
turtle.tracer(10)
#t.speed(0)


a = random.randint(5, 30)
b = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

for i in range(1, 30):
     t.ht()
     t.dot(a ,b)
     t.up()
     t.setx(random.randint(-390, 390))
     t.sety(random.randint(-240, 240))
     t.pd()
     a = random.randint(5, 30)
     b = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            
            




     
