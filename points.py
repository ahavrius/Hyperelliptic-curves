from HEC import *
from GF import *

class Point_of_HEC():
    curve: HEC
    field: GF
    x: int
    y: int
    is_inf: bool
    def __init__(self, x, y, curve):
        self.is_inf = False
        self.curve = curve
        self.field = curve.field
        self.x = x % self.field.p
        self.y = y % self.field.p

    def __str__(self):
        if self.is_inf:
            point_str = 'point = Infinity'
        else:
            point_str = 'x = ' + str(self.x) + ' y = ' + str(self.y)
        return  point_str + ' on ' + str(self.curve)

    @classmethod
    def infinit_point(cls, curve):
        elem = cls(0, 0, curve)
        elem.is_inf = True
        return elem

    def is_finit(self):
        return not self.is_inf

    def opposite(self):
        if self.is_inf:
            return self
        x = self.x
        y = -self.y - poly_calc(x, self.curve.h[::-1])
        return Point_of_HEC(x, y, self.curve)

    def belong_curve(self):
        if self.is_inf:
            return True
        x = self.x
        y = self.y
        return 0 == y^2 + y * poly_calc(x, self.curve.h[::-1]) - poly_calc(x, self.curve.f[::-1])

    def is_spacial(self):
        if self.is_inf:
            return True
        opposite = self.opposite()
        return self.x == opposite.x and self.y == opposite.y

    def is_ordinary(self):
        return not self.is_spacial()

class Point_of_Ring(Point_of_HEC):
    def __init__(self, x, y, poly):
        super().__init__(x, y, poly.curve)
        self.poly = poly

    @classmethod
    def infinit_point(cls, frac):
        elem = cls(0, 0, frac)
        elem.is_inf = True
        return elem



curve = HEC(7, 4, [4, 1], [3, 3, 3, 3, 3,3, 3])
pnt = Point_of_HEC(32, -1200, curve)
print(pnt)
print(Point_of_HEC.infinit_point(curve))

#pnt_ring = Point_of_Ring(32, -1200, curve)