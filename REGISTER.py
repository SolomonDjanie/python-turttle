from turtle import *
speed(0)
register_shape('quardrilateral',((5,2),(2,-0),(-4,9)))
turtlesize(8,9,9)
for k in range(1, 300 ):
    stamp()
    fd(10*k)
    lt(50*k)
    fd(15*k)
    lt(45*k)
