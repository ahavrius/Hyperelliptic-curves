from sympy.polys.domains import ZZ
from sympy.polys.galoistools import gf_normal, gf_degree
from GF import *
import numpy as np
import matplotlib.pyplot as plt

gf_normal([5, 10, 21, 5, -3], 5, ZZ)


class HEC_general():
    field: GF
    h: list
    f: list
    genus: int

    def __init__(self, p, n, h, f):
        self.field = GF(p, n)
        self.h_canonic(h)
        self.f_canonic(h, f)
        self.genus = gf_degree(f)/2 - 1

    def h_canonic(self, h):
        if (self.field.p == 2):
            self.h = self.field.reduce(h)
        else:
            self.h = []

    def f_canonic(self, h, f):
        if (self.field.p != 2):
            h_inv = [ i * mod_inv(4, self.field.p) for i in h]
            f = self.field.add(f, self.field.mul(h, h_inv))
        self.f = self.field.reduce(f)

    def is_canonic(self):
        return self.h == []

    def is_correct(self):
        u = np.arange(self.field.p)
        v = np.arange(self.field.p)
        h_reverse = self.h[::-1]
        f_reverse = self.f[::-1]
        h_deriv = deriv_poly(h_reverse)
        f_deriv = deriv_poly(f_reverse)
        res1 = pow(v, 2) + np.multiply(v, poly_calc(u, h_reverse)) - poly_calc(u, f_reverse)
        res2 = 2 * v + poly_calc(u, h_reverse)
        res3 = np.multiply(v, poly_calc(u, h_deriv)) - poly_calc(u, f_deriv)
        return sum((res1 == 0) & (res2 == 0) & (res3 == 0)) == 0

    def drow_curve(self):
        y, x = np.ogrid[-10:10:100j, -10:10:100j]
        plt.contour(x.ravel(), y.ravel(), pow(y, 2) + y * poly_calc(x, self.h[::-1]) - poly_calc(x, self.f[::-1]), [0])
        plt.grid()
        plt.show()

#    @classmethod

"""
#Example:
ff = GF(3, 4)
g = ff.mul([1], [1, 1, 1])
print(ff.reducing)
print(g)

crv = HEC_general(5, 12, [], [1, 0, 0])
print(crv.h)
print(crv.f)
crv.drow_curve()
print(crv.is_correct())
"""