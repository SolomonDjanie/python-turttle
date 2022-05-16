import turtle as t
t.bgcolor("black")
t.pencolor("lime")
t.pensize(5)
         
def square():
    for k in range (4):
        t.fd(k*1*1*1*1*1)
        t.lt(90)


square()
t.up()
t.bk(25)
t.rt(90)
t.fd(25)
t.pd()

for k in square():
    t.fd(10)
       
