import math
import turtle

'''
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
bob = turtle.Turtle()
square(bob)


def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
bob = turtle.Turtle()
square(bob,300)

def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
bob = turtle.Turtle()
polygon(bob,50,8)
'''
def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t,r,f,n):
    leng = 2*math.pi*r/n
    f(t,leng,n)
bob = turtle.Turtle()
circle(bob,80,polygon,200)




