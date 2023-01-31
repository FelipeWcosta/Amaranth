from amaranth import *
m = Module()
s = Signal()
print(s.eq(1))
a = Signal(8)
b = Signal(4)
print(Cat(a, b).eq(0))
print((a[:4]).eq(b))
print(Cat(a, a).bit_select(b, 2).eq(0b11))