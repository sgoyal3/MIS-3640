mport turtle
import math


def draw_shape(sides, length):
    for i in range(sides):
        turtle.forward(length)
        turtle.right(360 / sides)
        
draw_shape(2, 40)
draw_shape(10, 60)
draw_shape(12, 100)
turtle.mainloop()


def square(t, length):
    for i in range(500):
        t.fd(length)
        t.lt(91)
jack = turtle.Turtle()
square(jack,200)

turtle.mainloop()