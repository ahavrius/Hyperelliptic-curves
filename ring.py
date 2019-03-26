from HEC import *
from GF import *

class Ring():
    field: GF
    curve: HEC_general
    a: list
    b: list
    def __init__(self, a, b, curve):
        self.a = a
        self.b = b
        self.curve = curve
        self.field = curve.field


