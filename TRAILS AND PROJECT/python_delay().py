import turtle
import random




t = turtle.Turtle()


win = turtle.Screen()


win.bgcolor('blue')
win.title('Using turtle Delay method')
win.setup(width = 800, height = 500)


turtle.colormode(255)
t.speed(0)
t.shape('turtle')


a = random.randint(5, 30)
b = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

for i in range(1, 30):
     t.dot(a ,b)
     t.up()
     t.setx(random.randint(-390, 390))
     t.sety(random.randint(-240, 240))
     t.pd()
     a = random.randint(5, 30)
     b = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            
            


t.reset()
turtle.delay(100)

for i in range(1, 30):
     t.stamp()
     t.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
     t.up()
     t.setx(random.randint(-390, 390))
     t.sety(random.randint(-240, 240))
     t.pd()




     
