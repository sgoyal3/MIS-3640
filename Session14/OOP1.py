import math

class Point:
    """Represents a point in 2-D space.
    attributes: x, y
    """

my_point = Point()
print(type(my_point))

my_point.x = 3
my_point.y = 4

print(my_point.x, my_point.y)
my_point.x = 5

x = my_point.y
print(x)

import math

print('(%g, %g)' % (my_point.x, my_point.y))
distance = math.sqrt(my_point.x**2 + my_point.y**2)
print(distance)

def print_point(p):
    """Print a Point object in human-readable format."""
    print('({}, {}).'.format(p.x, p.y))
    
    
print_point(my_point)
    


def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.
    p1: Point
    p2: Point
    returns: float
    """
    pass






class Rectangle:
    """Represents a rectangle. 
    attributes: width, height, corner.
    """



def find_center(rect):
    """Returns a Point at the center of a Rectangle.
    rect: Rectangle
    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p




def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.
    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight




def print_rectangle(rect):
    print('width:', rect.width, 'height:', rect.height)
    print('the lower-left corner:')
    print_point(rect.corner)




def main():
    my_point = Point()
    # print(Point.__doc__)
    # my_point.x = 3
    # my_point.y = 4
    # print('My point', end=' ')
    # print_point(my_point)

    # print('Is my_point an instance of Point?', isinstance(my_point, Point))
    # print('Is my_point an instance of Rectangle?',
    #       isinstance(my_point, Rectangle))
    # print('Does my_point have an attribute x?', hasattr(my_point, 'x'))
    # print('Does my_point have an attribute z?', hasattr(my_point, 'z'))

    # box = Rectangle()
    # box.width = 100.0
    # box.height = 200.0
    # box.corner = Point()
    # box.corner.x = 0.0
    # box.corner.y = 0.0

    # print('Does box have an attribute x?', hasattr(box, 'x'))

    # print('Does box have an attribute corner?', hasattr(box, 'corner'))

    # print('Rectangle has these:', dir(box))

    # center = find_center(box)
    # print('center', end=' ')
    # print_point(center)

    # print(box.width)
    # print(box.height)
    # print('grow')
    # grow_rectangle(box, 50, 100)
    # print(box.width)
    # print(box.height)


if __name__ == '__main__':
    main()