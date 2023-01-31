from amaranth import *
print(Signal().shape())
print(Signal(4).shape())
print(Signal(0).shape())
foo = Signal()
print(foo.name)
foo2 = Signal(name = "second_foo")
print(foo2.name)