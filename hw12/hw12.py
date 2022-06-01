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
    def __iter__(self):
        res = 0.5 * (self.x + self.y + self.b)
        k1 = (res - self.x)
        k2 = (res - self.y)
        k3 = (res - self.b)
        result = (res * k1 * k2 * k3) * 0.5
        return result

e = Half(4, 5, 6)

print(e.__iter__)
