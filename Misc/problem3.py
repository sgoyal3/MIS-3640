import random

def Drunk_Walk(x,y,n):
    """
    x, y: the original location
    n: the number of intersections(steps)
    return the distance after n intersections(steps) from the origin
    """
    x = 0
    y = 0
    # creates the starting point (0,0)
    n = int(input('How many times would you like to move?'))
    for x,y in range(n):
        a = random.randint(1,4)
        if a == 1:
            y = y + 1
        if a == 2:
            x = x + 1
        if a == 3:
            y = y - 1
        if a == 4:
            x = x - 1
    distance = (x+y)
    print(distance)


