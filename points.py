from HEC import *
from GF import *

class Point_of_HEC():
    curve: HEC_general
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

    @classmethod
    def infinit_point(cls, curve):
        elem = cls(0, 0, curve)
        elem.is_inf = True
        return elem

    def is_finit(self):
        return not self.is_inf

    @classmethod
    def opposite(cls, point):
        if self.is_inf:
            return self
        x = point.x
        y = -point.y - poly_calc(x, point.curve.h[::-1])
        return cls(x, y, point.curve)

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
    def __init__(self, x, y, field):
        super().__init__(x, y, field)
