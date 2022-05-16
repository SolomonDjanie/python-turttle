from turtle import *
speed(0)
up()
lt(90)
fd(200)
rt(30)
pd()
pensize(3)
def Triang ():
    for k in range (3):
        rt(120)
        fd(400)


    up()
    rt(150)
    fd(480)
    pd()

    dot(150,'black')

    up()
    goto(213, 70)
    pd()

    dot(150,'black')

    up()
    goto(-215, 70)
    pd()

    dot(150,'black')

    up()
    goto(1, 50)
    pencolor('white')
    fd(330)
    rt(30)
    pd()

    color('white')
    begin_fill()
    for k in range (3):
        rt(120)
        fd(400)
    end_fill()

Triang()
hideturtle()
