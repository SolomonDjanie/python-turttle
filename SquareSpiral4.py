# SquareSpiral1.py - Draw a squra aprial
import turtle
t = turtle.Pen()
turtle.bgcolor('black')
#take pencolor from a user
shape_color = turtle.textinput('shape color','Enter your color please:')

#take angle side from a user
angle_size = turtle.numinput('angle size','Enter the size of the angle please:')


for x in range(int(range_num)):
    t.color(shape_color)
    t.fd(x)
    t.left(int(angle_size))
