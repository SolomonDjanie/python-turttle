import turtle


t = turtle.Pen()

win = turtle.Screen()

win.bgcolor('blue')




def drag (x, y):
    
    t.ondrag(None)
    
    t.width(10)
    t.goto(x, y)

    t.ondrag(drag)




t.ondrag(drag)
