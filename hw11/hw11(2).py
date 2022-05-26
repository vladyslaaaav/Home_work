class Point:
    x = 0
    y = 0
    b = 0
    def __init__(self, x_coord, y_coord, b_coord):
        self.x = x_coord
        self.y = y_coord
        self.b = b_coord


class Half(Point):

    @property
    def half(self):
        return 0.5 * (self.x + self.y + self.b)

e = Half(1, 4, 5)

print(e.half)

class Triangle(Half):

    def area(self):
        k1 = (e.half - x)
        k2 = (e.half - y)
        k3 = (e.half - b)
        res = (e.half * k1 * k2 * k3) * 0,5
        return res

e = Triangle(1, 4, 5)
print(e.area)


