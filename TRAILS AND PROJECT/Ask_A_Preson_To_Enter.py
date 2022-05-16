import turtle
t=turtle.Pen()
turtle.bgcolor("black")
colors = ["red","yellow","blue","green"]

#Ask the user's name using turtle's textinput pop-up window
your_name = turtle.textinput("Enter your name","What is your name?")

for x in range(100):
    t.pencolor(colors[x%4])
    t.penup()
    t.fd(x*4)
    t.pd()
    t.write(your_name,font=("ARIAL",int((x+4)/4),"bold"))
    t.lt(200)
                            
