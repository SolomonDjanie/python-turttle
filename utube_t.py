import turtle as t 

t.bgcolor('black')
t.pensize(3)
t.up()
t.fd(150)
t.rt(90)
t.fd(100)
t.lt(180)
t.pd()

t.color('red','red')
t.begin_fill()
for k in range(4):
    t.fd(200)
    t.circle(50,90)
t.fd(100)
t.lt(90)
t.fd(150)
t.rt(180)
t.end_fill()



t.color('white')
t.begin_fill()
t.shape('triangle')
t.shapesize(5,5,5)
t.end_fill()

