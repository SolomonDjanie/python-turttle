c
x = randrange(turtle.window_width()//2, tutle.window_width()//2)
y = randrange(turtle.window_heigth()//2, tutle.height_width()//2)


 up()
    setpos(x,y)
    pd()

    #head
    color('yellow')
    begin_fill()
    circle(50)
    end_fill()
    up()

    #left eye

    #mouth
    setpos(x-25,y+40)
    pd()
    color('black')
    width(10)
    goto(x-10, y+20)
    goto(x-10, y+20)
    goto(x-20, y+40)
    width(1)


    for k in range(50):
        x = random.randrange(-window_width()//2, window_width()//2)
        y = random.rangrange(-window_height()//2, window_heigth()//2)

