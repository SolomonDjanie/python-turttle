#import modules
import turtle, math

from turtle import *

pensize(4)

#set the radius
r1 = 300
r2 = 200

#create an empty list to store the values
px = []
py = []

#set the angles
startAngle = 0
endAngle = 2*math.pi

#number of points
n = 500

step_angle = 0

for k in range(n):
     x = r1*math.cos(step_angle)
     px.append(x)
     y = r2*math.sin(step_angle)
     py.append(y)

     step_angle -= (endAngle - startAngle)/(n-1)


up()
goto(r1, 0)
down()

for i in range(n):
     goto(px[i],py[i])







ht()
mainloop()


     
                   
