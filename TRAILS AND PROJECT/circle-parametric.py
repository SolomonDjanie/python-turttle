#import modules
import turtle, math

from turtle import *

pensize(4)

#set the radius
r = 200

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
     x = r*math.cos(step_angle)
     px.append(x)
     y = r*math.sin(step_angle)
     py.append(y)

     step_angle = (endAngle - startAngle)/(n-1)


up()
goto(r, 0)
down()

for i in range(n):
     goto(px[i],py[i])




ht()
mainloop()


     
                   
