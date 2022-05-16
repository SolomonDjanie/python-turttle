import turtle
t = turtle.Pen()
turtle.speed(200)
turtle.bgcolor('black')
colors = ["red","yellow","blue","green"]
for x in range(900):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)
