
import turtle
from turtle import *
import numpy as np
speed(0)




px = []
py = []
pu()

for k in np.arange(-20, 20 ,0.1):
     px.append(k**10)
     py.append(5*k**9)

goto(-20,400)
down()

for i in range(500):
     goto(px[i], py[i])
           

    


