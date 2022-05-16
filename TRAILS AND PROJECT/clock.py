import turtle as t
t.speed(0)

def four():
    t.pd()
    t.pensize(3)
    t.fd(20)
    
def one():
    t.pd()
    t.pensize(1)
    t.fd(15)


for k in range (12):
    t.pu()
    t.seth(k*30)
    t.fd(200)
    four()
    t.up()
    t.home()


for k in range(70):
    t.up()
    t.seth(k*6)
    t.fd(205)
    one()
    t.up()
    t.home()
t.ht()
