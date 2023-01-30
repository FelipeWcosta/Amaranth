from amaranth import *
print(Shape(width = 5, signed = False))
print(Shape(width = 12, signed = True))
print(unsigned(5) == Shape(width = 5, signed = False))
print(signed(12) == Shape(width = 12, signed = True))
print(Const(5).shape())
print(len(Const(5)))
print(Shape.cast(5))
print(C(0, 3).shape())