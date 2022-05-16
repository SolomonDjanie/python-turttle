from turtle import*
bgcolor('blue')
pensize(3)

speed(0)            


up()
rt(90)
fd(50)
lt(90)
bk(50)
pd()
def book ():
     color('violet','purple')
     begin_fill()

     fd(150)
     lt(90)
     fd(200)
     lt(90)
     fd(150)
     lt(90)
     fd(200)
     end_fill()





     color('violet','white')
     begin_fill()
     rt(45)
     fd(30)
     lt(135)
     fd(150)
     lt(45)
     fd(30)
     lt(135)
     fd(150)
     lt(45)
     fd(30)
     end_fill()


     color('violet','purple')
     begin_fill()
     rt(135)
     fd(200)
     rt(45)
     fd(30)
     rt(135)
     fd(200)
     rt(45)
     fd(30)
     end_fill()


     rt(135)
     fd(200)
     rt(45)
     fd(30)
     rt(135)
     up()
     fd(50)
     lt(90)
     fd(55)
     pd()

     def music ():
          pensize(5)
          color('black')
          begin_fill()
          circle(5)
          fd(10)
          lt(90)
          fd(20)
          lt(90)
          fd(5)
          lt(90)
          fd(20)
          bk(20)
          lt(120)
          pensize(1)
          circle(-15, 90)
          lt(55)
          fd(5)
          lt(90)
          circle(15, 100)
          fd(10)
          lt(87)
          fd(10)
          end_fill()


     music()


     up()
     fd(80)
     rt(90)
     fd(55)
     lt(90)

     pd

     color('goldenrod')
     begin_fill()
     write('Cooding',False,font=("Times New Roman", 20, "normal"))

     up()
     fd(22)
     pd()
     write('With',False,font=("Times New Roman", 20, "normal"))

     up()
     fd(22)
     pd()
     write('Python',False,font=("Times New Roman", 20, "normal"))

        
book()
ht()

