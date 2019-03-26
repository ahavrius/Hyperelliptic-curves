from HEC import *
from GF import *

class PolyRing():
    field: GF
    curve: HEC
    a: list
    b: list
    def __init__(self, a, b, curve):
        self.curve = curve
        self.field = curve.field
        self.a = a
        self.b = b
        self.simlify()

    def simlify(self):
        self.a = self.field.reduce(self.a)
        self.b = self.field.reduce(self.b)

    def conjugate(self):
        field = self.field
        b = field.minus(self.b)
        a = field.add(self.a, field.mul(b, self.curve.h))
        return PolyRing(a, b, self.curve)

    def norm(self):
        res = self * self.conjugate()
        if res.b:
            print("Ring.norm Warning: norm worked incorrect for some reasons")
        return res.a

    def get_degree(self, norma = 0):
        if norma == 0:
            norma = self.norm()
        return len(norma)-1

    def __mul__(self, other):
        if self.curve != other.curve or self.field != other.field:
            return None
        field = self.field
        curve = self.curve
        a = field.add(field.mul(self.a, other.a), field.mul(field.mul(self.b, other.b), curve.f))
        b = field.add(field.mul(self.a, other.b), field.mul(self.b, other.a))
        return PolyRing(a, field.sub(b, curve.h), curve)

    def __add__(self, other):
        if self.curve != other.curve or self.field != other.field:
            return None
        field = self.field
        a = field.add(self.a, other.a)
        b = field.add(self.b, other.b)
        return PolyRing(a, b, self.curve)

    def __sub__(self, other):
        if self.curve != other.curve or self.field != other.field:
            return None
        field = self.field
        a = field.sub(self.a, other.a)
        b = field.sub(self.b, other.b)
        return PolyRing(a, b, self.curve)

    def __str__(self):
        a = self.a[::-1]
        b = self.b[::-1]
        a_str = [' {}u^{} '.format(a[i], i) for i in range(len(a)) if a[i] != 0]
        b_str = [' {}u^{} '.format(b[i], i) for i in range(len(b)) if b[i] != 0]
        if not a_str and not b_str:
            res = 'G(u, v) = 0'
        else:
            res = 'G(u, v) = ' + '+'.join(a_str) + '+ v(' + '+'.join(b_str) + ')'
        res = res.replace('= +', '= ')
        res = res.replace('+ -', '- ')
        res = res.replace('+ v()', '')
        return res

"""
#Exanple
crv = HEC(5, 3, [3, 3, 3], [1, 0, -5, 0, 4, 0])
elem = PolyRing([4, 0, 9], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], crv)
print(elem)
print(elem.conjugate())
print(elem.norm())
print(elem.get_degree())
"""