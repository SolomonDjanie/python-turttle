from turtle import *
speed(0)
pensize(5)
up()
lt(90)
fd(50)

pd()

dot(60,'white')
dot(50,'blue')

up()
lt(160)
fd(30)
fd(100)
pd()

color('yellow')
begin_fill()
pencolor('yellow')
pensize(2)
rt(193)
fd(119)

rt(15)
circle(30,125)
rt(167)
fd(150)
rt(266)
circle(150, -115)
end_fill()


color('lime')
begin_fill()
pencolor('lime')

circle(145, -100)
lt(74)
fd(133)
lt(152)
circle(-30, -115)
lt(17)
fd(115)
end_fill()

up()
pencolor('red')

lt(100)
circle(144 , 120)
pd()

color('red')
begin_fill()
circle(150, 141)
lt(75)
fd(132)
rt(30)
circle(30 , -110)
lt(187)
fd(151)
end_fill()

hideturtle()
