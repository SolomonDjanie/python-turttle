from turtle import*
speed(0)
up()
rt(90)
fd(100)
lt(90)
pd()

bgcolor("blue")
pensize(5)
shape("turtle")

def tri():

     color("black","red")
     begin_fill()
     lt(50)
     fd(40)
     lt(120)
     fd(40)
     lt(120)
     fd(40)
     lt(90)
     
     up()
     fd(40)
     pd()
     end_fill()


tri()

for k in range(35):
     tri()
     rt(10)
     


