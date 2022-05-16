import turtle as t
t.speed(9000)
t.bgcolor("yellow")
t.pencolor("white")
t.lt(90)
t.up()
t.bk(100)
t.rt(90)

t.pd()
t.pencolor("maroon")
t.color("maroon","maroon")
t.begin_fill()
for k  in range (2):
    t.lt(90)
    t.fd(200)
    t.lt(90)
    t.fd(25)

t.end_fill()

t.lt(180)
t.fd(25)

t.up()
t.fd(50)   
t.pd()

t.color("maroon","maroon")
t.begin_fill()
t.pencolor("maroon")

for k  in range (2):
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.fd(25)

t.end_fill()

t.color("orangered","orangered")
t.begin_fill()
t.pencolor("maroon")
t.up
t.rt(90)
t.fd(200)
t.rt(90)
t.fd(25)

t.rt(76)
t.fd(206)

t.rt(106)
t.fd(25)
t.rt(74)
t.fd(206)
t.end_fill()
t.hideturtle()
