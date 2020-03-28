from turtle import *

def drawstar(x, y):
    pu()
    goto(x, y)
    pd()
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)


for x in range(0, 250, 50):
    drawstar(x, 0)

done()
