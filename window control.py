import turtle
from turtle import *

win = turtle.Screen()
win. bgcolor('black')
win.bgcolor()

for k in range(4):
    fd(200)
    lt(90)

color('blue')
begin_fill()
for k in range(4):
    fd(200)
    rt(90)
end_fill()

color('yellow')
begin_fill()
for k in range(4):

    rt(90)
    fd(200)
end_fill()




color('red')
begin_fill()
for k in range(4):

    lt(90)
    fd(200)
end_fill()

color('green')
begin_fill()
for k in range(4):

    
    fd(200)
    lt(90)
end_fill()
