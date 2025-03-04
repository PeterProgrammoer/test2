import turtle
import math

t = turtle.Turtle()

t.pu()
t.goto(0,0)
t.pd()

i = 7
e = 360/i
for g in range(i):
    t.fd(100)
    t.lt(e)

turtle.done()
    