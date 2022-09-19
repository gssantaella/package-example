

class Point2(object):
    """docstring for Point2"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point2({self.x}, {self.y})'


class Vector2(object):
    """docstring for Vector2"""
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector2({self.x}, {self.y})'

    @classmethod
    def create_from_points(cls, u, v):
        return Vector2(v.x - u.x, v.y - u.y)

    @property
    def length(self):
        return (self.x**2 + self.y**2)**0.5
    


if __name__ == '__main__':
    p1 = Point2(0, 0)
    print(p1)

    p2 = Point2(0, 1)
    print(p2)

    v1 = Vector2(1, 0)
    print(v1)

    v2 = Vector2.create_from_points(p1, p2)
    print(v2)
    print(v2.length)