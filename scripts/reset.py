from amaranth import *
print(Signal(4).reset)
print(Signal(4, reset = 5).reset)
print(Signal().reset_less)
print(Signal(reset_less = True).reset_less)