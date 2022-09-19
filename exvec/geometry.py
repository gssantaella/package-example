
from vector import Point2, Vector2
import math

class Circle(object):
    """docstring for Circle"""
    def __init__(self, origin, radius):
        self.origin = origin
        self.radius = radius
    
    def __str__(self):
        return f'Circle({self.origin}, r: {self.radius})'


    @property
    def area(self):
        return round(math.pi * self.radius**2, 2)

    @property
    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)
    



if __name__ == '__main__':
    p1 = Point2(1, 0)
    print(p1)

    c1 = Circle(p1, 3)
    print(c1)
    print(c1.area)
    print(c1.perimeter)