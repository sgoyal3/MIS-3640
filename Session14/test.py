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