import math
import turtle


def polygon(t,step_length,turn,step):
    for i in range(int(step)):
        t.fd(step_length)
        t.lt(turn)
bob = turtle.Turtle()

def arc(t, r, angle,x):
    circle_length = math.pi * 2 * r
    step_length = circle_length / 360*x
    step = angle/x
    polygon(t, step_length, x, step)

arc(bob, 100, 90,1)