import turtle as t
t.speed(2)
t.up()
t.lt(90)
t.fd(298)
t.rt(90)
t.pd()

#step 1
t.color("dimgray","lightblue")
t.begin_fill()
t.rt(40)
t.fd(250)
t.rt(50)
t.fd(70)
t.rt(130)
t.fd(250)
t.rt(50)
t.up()
t.fd(70)
t.pd()
t.lt(130)
t.fd(250)
t.lt(50)
t.fd(70)
t.lt(130)
t.fd(250)
t.end_fill()

t.bk(220)

t.color("dimgray","lightblue")
t.begin_fill()
t.rt(130)
t.fd(300)
t.lt(90)
t.fd(340)
t.lt(90)
t.fd(300)
t.bk(300)

t.rt(90)
t.fd(50)
t.rt(90)
t.fd(60)
t.rt(90)
t.fd(440)
t.rt(90)
t.fd(60)
t.rt(90)
t.fd(50)
t.end_fill()

t.fd(190)
t.lt(90)
t.up()
t.fd(100)
t.pd()


t.color("dimgray","lightblue")
t.begin_fill()
t.circle(15,360)
t.end_fill()


t.up()
t.bk(100)
t.rt(90)
t.bk(15)
t.lt(90)
t.fd(200)
t.pd()
t.dot(100,"black")

t.hideturtle()
