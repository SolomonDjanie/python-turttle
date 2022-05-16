import turtle


win=turtle.Screen()
win.title("Handling keypresses!")
win.bgcolor("lightgreen")
win.setup(400,500)


tess = turtle.Turtle()


def h1():
  tess.forward(30)


def h2():
   tess.left(45)


def h3():
   tess.circle(45)

def h4():
   win.bye()




win.onkey(h1, "Up")
win.onkey(h2, "Left")
win.onkey(h3, "Right")
win.onkey(h4, "q")



win.listen()
turtle.mainloop()
