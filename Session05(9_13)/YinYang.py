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


def Yang(t, r):
    t.penup()
    t.goto(0, 200)
    t.pendown()
    t.circle(50, 180)

def Yin(t, r):
    t.circle(50, 180)

def Upper(t, r):
    t.penup()
    t.goto(0, 120)
    t.pendown()
    t.circle(35, 360)


def Lower(t, r):
    t.penup()
    t.goto(0, 30)
    t.pendown()
    t.circle(35, 360)

circle(Jack, 100)

Yin(Jack, 100)
Yang(Jack, 100)
Upper(Jack, 100)
Lower(Jack, 100)