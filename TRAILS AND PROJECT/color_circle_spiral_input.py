#colourcirclespirall -circlespiral
import turtle
t=turtle.Pen()
turtle.bgcolor("black")


#take pencolor from the user
shape_color = turtle.textinput("shape color","Enter your shape color : ")

#take range number from the user
range_num = turtle.textinput("range number","Enter your range number : ")

#take angle size from the user
angle_size = turtle.textinput("angle size","Enter your angle size : ")


for i in range(int(range_num)):
    t.pencolor(shape_color)
    t.circle(i)
    t.left(int(angle_size))
    
