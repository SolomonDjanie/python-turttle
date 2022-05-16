#importing turtle  module
import turtle as t
t.bgcolor("black")

t.pensize(5)
t.home()


#first_rhombus
t.color("red","red")
t.begin_fill()
for k in range(2):
    t.forward(200)
    t.right(60)
    t.forward(200)
    t.right(120)
t.end_fill()

#second_rhombus
t.color("red","red")
t.begin_fill()
for k in range(2):
    t.bk(200)
    t.left(60)
    t.bk(200)
    t.left(120)
t.end_fill()




#third rhombus
t.color("red","red")
t.begin_fill()
t.left(60)
for k in range(2):
    t.forward(200)
    t.left(60)
    t.forward(200)
    t.left(120)
t.end_fill()
