from amaranth import *
ten = Const(10)
minus_two = C(-2)
print(ten.shape())
print(minus_two.shape())
print(C(0).shape())
print(Const(360, unsigned(8)).value)