from HEC import *
from GF import *
from ring import *

class PolyFract:
    field: GF
    curve: HEC
    top: PolyRing
    button: PolyRing

    def __new__(cls, top, button):
        top.simlify()
        button.simlify()
        if top.field ==  button.field and top.curve == button.curve and not (button.a == [] and button.b == []):
            return super(PolyFract, cls).__new__(cls)

    def __init__(self, top, button):
        self.field = top.field
        self.curve = top.curve
        self.top = top
        self.button = button
        self.simlify()

    def simlify(self):
         self.top.simlify()
         self.button.simlify()

    def __eq__(self, other):
        return self.top == other.top and self.button == other.button and self.field == other.field and self.curve == other.curve

    def __str__(self):
        top_str = str(self.top)
        button_str = str(self.button)
        len_sep = max(len(top_str), len(button_str))
        separator = "".join(['-' for i in range(len_sep)])
        return top_str + '\n' + separator + '\n' + button_str
#def __add__
#def __sub__
#def __mul__


curve = HEC(7, 4, [4, 1], [3, 3, 3, 3, 3,3, 3])
poly1 = PolyRing([1, 0, 1], [3, -5, 1], curve)
poly2 = PolyRing([2, 0, 0, 1], [4, 0, 3, 0, 0, 0], curve)
fract = PolyFract(poly1, poly2)
print (fract)
