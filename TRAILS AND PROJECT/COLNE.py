import turtle

t = turtle.getturtle()
t.begin_poly()


for k in range(4):
    t.fd(50)
    t.lt(90)






t.end_poly()
square = t.get_poly()
turtle.register_shape("mysquare",square)



t.up()
t.bk(300)
t.lt(90)
t.fd(290)
t.rt(90)
t.pd()


for k in range(10):
    t.shape("mysquare")
    t.up()
    t.stamp()
    t.fd(55)





t.up()
t.rt(90)
t.fd(105)
t.rt(90)
t.fd(500)

t.pd()


for k in range(10):
    t.shape("mysquare")
    t.up()
    t.stamp()
    t.fd(55)

