# 8.2. Right triangle class

from math import sqrt
import matplotlib.pyplot as plt

class RightTriangle:
    def __init__(self,a,b):

        self.a = a
        self.b = b
        if a<0 or b<0:
            raise ValueError
        self.c = sqrt(self.a**2+self.b**2)
    def plot_triangle(self):
        f = [0,0,self.a,0]
        d = [0,self.b,0,0]
        plt.plot(f,d)
        plt.show()

def test_RightTriangle():
    success = False
    try:
        triangle3 = RightTriangle(1,-1)
    except ValueError:
        success = True
    assert success
test_RightTriangle()

#b)
print("b)")
triangle1 = RightTriangle(1,1)
triangle2 = RightTriangle(3,4)
print(triangle1.c)
print(triangle2.c)
v = triangle2.plot_triangle()

"""
Run example:

user$ python3 right_triangle.py

output:
b)
1.4142135623730951
5.0

"""
