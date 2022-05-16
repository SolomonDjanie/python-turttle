#import package
import turtle


#method to action
def fxn(x,y):

    #some motion
    turtle.right(144)
    turtle.fd(100)
    turtle.dot(2)

#turtle speed to slowest
turtle.speed(1)


#motion
turtle.fd(100)


#allow user to click
#for some action
turtle.onclick(fxn)




#screen object
win = turtle.Screen()


#method to perform action
def fxn (x, y):
    turtle.goto(x, y)
    turtle.write(str(x)+","+str(y))



#onclick action
win.onclick(fxn)
win.mainloop()
