import turtle
t=turtle.Pen()
turtle.bgcolor("black")
colors=["red","yellow","blue","green","green","goldenrod","navy","olive","orangered","cyan"]

#Ask the user's name using using turtle's numinput pop_up window
polygon_side = int(turtle.numinput("Enter polygon side","What is your polygon side?"))


                   

for k in range(polygon_side):
    t.color(colors[k%polygon_side])
    t.fd(200)
    t.lt(360/polygon_side)
