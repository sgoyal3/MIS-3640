import math
from math import sqrt #I don't know why import math won't work, but apparently I needed to add this. 

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

r = (b**2) - (4*a*c)

if r > 0:
    x1 = (((-b) + sqrt(r))/(2*a))
    x2 = (((-b) - sqrt(r))/(2*a))
    print("Are 2 roots: %f and %f" % (x1, x2))
elif r == 0: #use an elif statement here, though we haven't technically covered it yet
    x = (-b) / 2*a
    print("There is one root: ", x)
else:
    print("No roots, discriminant is < 0.")

