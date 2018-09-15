import math
import turtle
import turtle

Jack = turtle.Turtle() 


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)


def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)


def flower(t, n, r, angle):
    for i in range(n):
        t.penup()
        t.goto(0, 100)
        t.pendown()
        petal(t, r, angle)
        t.lt(360.0 / n)

#Then we needed to shift the circle


Jack = turtle.Turtle()

circle(Jack, 100)
flower(Jack, 7, 100.0, 60.0)

