#import modliles
from turtle import *
import turtle,math
import random


t = turtle.Turtle()


t = turtle.getturtle()
win = turtle.Screen()
win.bgcolor('blue')
win.title('Using turtle tracer method')
win.setup(width = 800, height = 500)




pencolor('lime')
pensize(2)
speed(0)

intitial_value = 0
final_value = 100 * math.pi
steps = (final_value - intitial_value) / 500
x_values = []

#calculate the x value
for k in range(10000):
     intitial_value = intitial_value + steps
     x_values.append(intitial_value)



#calculate the y value

y_values = []
for k in range(10000):
     y_values.append(100 * math.tan\(x_values[k] / (10 * math.pi)))
     y_values.append(100 * math.sin(x_values[k] / (10 * math.pi)))


for i in range(10000):
     goto(x_values[i], y_values[i])






turtle.mainloop()

     
