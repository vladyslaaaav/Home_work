class Point:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.name = x
        self.name = y

    @property
    def res(self):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError



p1 = Point(6, 3)










