from HEC import *
from GF import *
from ring import *

class PolyFract():
    field: GF
    curve: HEC
    top: PolyRing
    button: PolyRing

    def __new__(cls, top, button):
        #if top.field == button.field and top.curve == button.curve:
        return PolyFract.__init__(cls, top, button)

    def __init__(self, top, button):
        self.field = top.field
        self.curve = top.curve
        self.top = top
        self.button = button



curve = HEC(7, 4, [4, 1], [3, 3, 3, 3, 3,3, 3])
poly1 = PolyRing([1, 0, 1], [3, -5, 1], curve)
poly2 = PolyRing([2, 0, 0, 1], [4, 0, 3, 0, 0, 0], curve)
fract = PolyFract(poly1, poly2)
print (fract)

class PolyFract():
    def __new__(cls, top, button):
        #if top.field == button.field and top.curve == button.curve:
        return PolyFract.__init__(cls, top, button)
    def __init__(self, top, button):
        self.top = top
        self.button = button