from turtle import*
pensize(2)
speed(0)
pencolor('black')
def house ():
    color('black','orange')
    begin_fill()
    lt(135)
    fd(100)
    lt(65)
    fd(100)
    lt(110)
    fd(100)
    lt(72)
    fd(109)
    end_fill()
    up()
    bk(109)
    rt(202)
    pd()
    color('black','deeppink')
    begin_fill()
    fd(120)
    rt(125)
    fd(95)
    rt(105)
    fd(100)
    end_fill()
    color('black','blue')
    begin_fill()
    rt(40)
    fd(150)
    rt(90)
    fd(116)
    rt(90)
    fd(150)
    rt(90)
    fd(116)
    rt(90)
    fd(150)
    rt(90)
    fd(35)
    end_fill()
    color('black','lime')
    begin_fill()
    rt(90)
    fd(90)
    lt(90)
    fd(50)
    lt(90)
    fd(90)
    end_fill()
    color('black','yellow')
    begin_fill()
    lt(90)
    fd(85)
    lt(20)
    fd(110)
    lt(70)
    fd(150)
    lt(110)
    fd(110)
    lt(70)
    fd(150)
    end_fill()

    lt(110)
    fd(50)
    lt(70)
    up()
    fd(75)
    pd()
    color('black','brown')
    begin_fill()
    fd(35)
    rt(75)
    fd(25)
    rt(106)
    fd(35)
    rt(75)
    fd(25)
    end_fill()
    up()
    rt(90)
    fd(180)
    write('house',True,font=("Arila", 20, "normal"))


def sun ():
    rt(15)

    goto(210, 150)
    pd()
    for k  in range(1):
        
        fd(150)
        bk(75)
        
        for k in range (4):
            lt(45)
            fd(55)
            bk(55)
            lt(45)
            fd(75)
            bk(75)

    bk(35)
    rt(85)
    color('black','yellow')
    begin_fill()
    circle(35)
    end_fill()

    up()
    goto(245, 230)
    write('Sun',True,font=("Arila", 20, "normal"))


def tree ():
    up()
    rt(90)
    fd(250)
    rt(91)
    fd(150)
    
    pd()
    color('black','green')
    begin_fill()
    for k  in range (3):
        rt(121)
        fd(70)
    end_fill()


    color('black','green')
    begin_fill()
    up()
    bk(35)
    pd()
    end_fill()
    color('black','green')
    begin_fill()
    lt(121)
    fd(75)
    rt(121)
    fd(75)
    rt(121)
    fd(75)
    up()
    rt(121)
    fd(75)
    pd()
    rt(121)
    fd(35)
    end_fill() 
    color('black','green')
    begin_fill()
    lt(120)
    fd(80)
    rt(118)
    fd(80)
    rt(120)
    fd(80)
    bk(80)
    lt(118)
    
    end_fill()
    bk(30)
    color('black','brown')
    begin_fill()
    lt(91)
    fd(50)
    lt(90)
    fd(20)
    lt(91)
    fd(50)
    end_fill()
    bk(50)
    rt(90)
    up()
    goto(220,-150)
    pd()
    write('Tree',False,font=("Arila", 20, "normal"))
   

    
house()
sun()
tree()















