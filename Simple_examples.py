import turtle as t
t.pensize(2)
t.bgcolor("yellow")
t.pencolor("blue")
t.shape("turtle")
t.speed(600)

for k in range(600):
    t.stamp()
    t.fd(100+k)
    t.circle(90)



t.speed(900)
t.shape("arrow")
t.pencolor("red")
for k in range(600):
    t.stamp()
    t.fd(100+k)
    t.circle(90)
