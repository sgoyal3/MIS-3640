import turtle
Jack = turtle.Turtle()

# Jack.fd(100)
# Jack.lt(90)
# Jack.fd(100)
# Jack.lt(90)
# Jack.fd(100)
# Jack.lt(90)
# Jack.fd(100)

# Using for statements
# for i in range(4):
#     print('Hello')

# def square(x):
#     for i in range(4):
#         x.fd(100)
#         x.lt(90)

# square(Jack)

# def polygon(x, n, length):
#     angle = 360 / n
#     for i in range(n):
#         x.fd(length)
#         x.lt(angle)

# polygon(Jack, 7, 70)

# #Circle

# import math

# def circle(x, r):
#     circumference = 2 * math.pi * r
#     n = int(circumference / 3) + 1
#     length = circumference / n
#     polygon(x, n, length)

# circle(Jack, 30)

# def arc(x, r, angle): 
#     arc_length = 4 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     Line_length = arc_length / n
#     Line_angle = angle / n
#     for i in range(n):
#         x.fd(Line_length)
#         x.lt(Line_angle)
# arc(Jack, 300, 30)
import math
def polyline(x, n , length, angle):
    for i in range(n):
        x.fd(length)
        x.fd(angle)

def polygon(x, n, length):
    angle = 360.0 / n
    polyline(x, n, length, angle)

def arc(x, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(x, n, step_length, step_angle)

def circle(x, r):
    arc(x, r, 360)


