from amaranth import *


class LEDBlinker(Elaboratable):
    def elaborate(self, plataform):
        m = Module()

        led = plataform.request("Led")

        half_freq = int(plataform.default_clk_frequency // 2)
        timer = Signal(range(half_freq + 1))

        with m.If(timer == half_freq):
            m.d.sync += led.eq(~led)
            m.d.sync += timer.eq(0)
        with m.Else():
            m.d.sync += timer.eq(timer + 1)

        return m
