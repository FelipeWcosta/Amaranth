from amaranth import *

class upCounter(Elaboratable):
  def __init__ (self, limit):
    self.limit = limit

    #Ports
    self.en = Signal()
    self.ovf = Signal()

    #State
    self.count = Signal()

  def elaborate(self, plataform):
    m = Module()

    m.d.comb += self.ovf.eq(self.count == self.limit)

    with m.If(self.en):
      with m.If(self.ovf):
        m.d.sync += self.count.eq(0)
      with m.Else():
        m.d.sync += self.count.eq(self.count + 1)
      
    return m