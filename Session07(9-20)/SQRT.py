import math

def mysqrt(a, x):
    epsilon = 0.0000001
    while True:
        # print(x)
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            return y
        x = y


def test_square_root(a):
    print('a   mysqrt(a)    math.sqrt(a)    diff')
    print('________________________________________')
    for z in range(1, 10):
        a = z
        b = mysqrt(a, z)
        c = math.sqrt(a)
        d = abs(b - c)
        print('{:f} {:f} {:f} {:f}'.format(a,b,c,d))

test_square_root(4)
