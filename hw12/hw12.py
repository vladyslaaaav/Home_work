class Point:
    _x = 0
    _y = 0

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        if not isinstance(new_x, (int, float)):
            raise TypeError
        self._x = new_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        if not isinstance(new_y, (int, float)):
            raise TypeError
        self._y = new_y


class Line:
    _begin = None
    _end = None

    def __init__(self, begin_point, end_point):
        self.begin = begin_point
        self.end = end_point

    @property
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, new_begin_point):
        if not isinstance(new_begin_point, Point):
            raise TypeError
        self._begin = new_begin_point

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, new_end_point):
        if not isinstance(new_end_point, Point):
            raise TypeError
        self._end = new_end_point

    @property
    def length(self):

        k1 = (self.begin.x - self.end.x) ** 2
        k2 = (self.begin.y - self.end.y) ** 2
        res = (k1 + k2) ** 0.5

        return res


class Triangle:
    _point_a = None
    _point_b = None
    _point_c = None
    _sides = []
    _idx = 0

    def __init__(self, _point_a, _point_b, _point_c):
        self._point_a = _point_a
        self._point_b = _point_b
        self._point_c = _point_c
        self._line_a = Line(_point_c, _point_b)
        self._line_b = Line(_point_c, _point_a)
        self._line_c = Line(_point_b, _point_a)

    def __iter__(self):
        self._sides = [self._line_a.length, self._line_b.length, self._line_c.length]
        return self

    def __next__(self):
        try:
            result = self._sides[self._idx]
        except IndexError:
            raise StopIteration
        else:
            self._idx += 1
            return result

    @property
    def point_a(self):
        return self._point_a

    @point_a.setter
    def point_a(self, new_point_a):
        if not isinstance(new_point_a, Point):
            raise TypeError
        self._point_a = new_point_a

    @property
    def point_b(self):
        return self._point_b

    @point_b.setter
    def point_b(self, new_point_b):
        if not isinstance(new_point_b, Point):
            raise TypeError
        self._point_b = new_point_b

    @property
    def point_c(self):
        return self._point_c

    @point_c.setter
    def point_c(self, new_point_c):
        if not isinstance(new_point_c, Point):
            raise TypeError
        self._point_c = new_point_c

    @property
    def triangle_area(self):
        """
        The area of the triangle on three sides
        """
        p = (self._line_a.length + self._line_b.length + self._line_c.length) / 2
        s = ((p * (p - self._line_a.length) * (p - self._line_b.length) * (p - self._line_c.length)) ** 0.5)
        return s


a = Point(3, 4)
b = Point(4, -2)
c = Point(-3, 7)

triangle1 = Triangle(a, b, c)

for i in triangle1:
    print(i)
