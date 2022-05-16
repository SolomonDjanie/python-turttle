import turtle as t
import random

t.title('Fibonacci Spiral By SOLOMON')

t.bgcolor("blue")

def square (L):
   for k in range(4):
       t.up()
       t.fd(L)
       t.lt(90)
       t.pd()


def sq_arc(L):
    square(L)
    t.circle(L, 90)



#fibonacci series
L = [1, 2, 3, 5, 8,  13, 21, 34, 55, 89, 144, 233, 377, 610, ]

t.up()
t.goto(-150, 100)
t.pd()


for i in L:
    t.color('red')
    sq_arc(i)
   

            
