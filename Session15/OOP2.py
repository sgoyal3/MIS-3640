#Exercise 2:

import math

class Point:
    """Represents a point in 2-D space.
    attributes: x, y
    """
my_point = Point()
print(type(my_point))

my_point.x = 3
my_point.y = 4


#Part A: Write a definition for a class named circle
#where center is a point object and radius is a number

class Circle:
    """Represents a circle.

    Attributes: center, radius"""
    """ radius """
    center = Point()
    
#Part B: 

myCircle = Circle()
myCircle.center.x = 150
myCircle.center.y = 100
myCircle.radius = 75

#Part C: Write a function named point_in_circle that takes a Circle and a Point and returns True if the Point lies in 
# or on the boundary of the circle. (need dbp function)

def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.
    p1: Point
    p2: Point
    returns: float
    """
    x_diff = p2.x - p1.x
    y_diff = p2.y - p1.y
    distance = math.sqrt(x_diff**2 + y_diff ** 2)
    return distance

def point_in_circle(point, Circle):
    c = Circle.center
    p = point
    dis = distance_between_points(c,p)
    print(dis)
    if dis <= Circle.radius:
        return True
    else:
        print("Point not within/on boundaries of circle")

#Part D: Write function named rect_in_circle that takes a Circle and a Rectangle and returns True if the Rectangle lies 
# entirely in or on the boundary of the circle.

class Rectangle:
    """Represents a rectangle. 
    attributes: width, height, corner.
    """
    
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def rect_in_circle(Circle,Rectangle):
    C=Circle
    R=Rectangle
    
    Corner1=R.corner
    Corner2=R.corner
    Corner3=R.corner
    Corner4=R.corner
    
    Corner2.x=Corner1.x+width
    Corner4.y=Corner2.y-height
    Corner3.x=Corner4.x-width
    
    #Python isn't recognizing my attributes here though.
    
    if point_in_circle(C,Corner1):
        if point_in_circle(C,Corner2):
            if point_in_circle(C,Corner3):
                if point_in_circle(C,Corner4):
                    return True
                    
#Section E: Couldn't get the prior function to run as well,
#but the code made sense, however it's returning syntax errors




    
