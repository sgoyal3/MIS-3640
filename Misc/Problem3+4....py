import random
import turtle
import math

SiddyG =turtle.Turtle()
""" First we must import turtle and create the four directions """

def North(t):
    """ Walk North 10 units """
    t.setheading(0)
    t.fd(10)

def East(t):
    """ Walk East 10 units """
    t.setheading(90)
    t.fd(10)

def South(t):
    """ Walk South 10 units """
    t.setheading(180)
    t.fd(10)

def West(t):
    """ Walk West 10 units """
    t.setheading(270)
    t.fd(10)
        
def drunkard_walk(x, y, n):
    x1 = 0
    y1 = 0
    n = int(input('How many times would you like to move?'))
    """ This is our starting origin point"""
    xy = []
    """ This empty list will allow us to put the directions into a list"""
    for i in range(n):
        """ For the number of intersections you request (n), python will compute the following commands """
        direction = random.randint(1, 4)
        """ This chooses a random integer 1 through 4, representative of the chosen direction """
        xy.append(direction)
        """ This will append or add the random integer chosen for each n to the list we created earlier """
        if direction == 1:
            North(SiddyG)
            y1 += 1
        elif direction == 2:
            South(SiddyG)
            y1 -= 1
        elif direction == 3:
            East(SiddyG)
            x1 += 1
        elif direction == 4:
            West(SiddyG)
            x1 -= 1
        
    print(x1, y1)
    print(xy)
    distance_x = (abs(x1-x)) ** 2
    distance_y = (abs(y1-y)) ** 2
    distance = math.sqrt(distance_x + distance_y)
    print(distance)
    print("After", n, "intersections, he's", distance, "blocks from where he started.")

drunkard_walk(x,y,n)
turtle.mainloop()