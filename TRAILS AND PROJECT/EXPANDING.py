import turtle as t


def triangle (size,x,y):
    t.pensize(3)
    t.color("blue")


    for k in range(3):
        t.fd(size+k)
        t.lt(120)
        
    
    t.up()
    t.goto(x,y)
    t.pd()

size =50
x, y = 15, 15
    
for k in range(1,20):
    triangle(size, -x*k, -y*k)
    size += abs(-x-y)





turtle.done()
              
