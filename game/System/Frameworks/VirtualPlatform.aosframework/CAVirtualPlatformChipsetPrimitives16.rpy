#
# CAVirtualPlatformChipsetPrimitives.rpy
# Virtual Platform (Candella)
#
# (C) 2021 Marquis Kurt. A/ll rights reserved.
#

init offset = -50
init python in CAVirtualPlatform:

    class CAVirtualAnd16Primitive(CAVirtualChip):
        """A primitive chip that performs a logical AND operation over 16 bits."""
        def __init__(self, a, b):
            if len(a) != 16 or len(b) != 16:
                raise CAVirtualChipBusError("And16: Expected inputs of bus length 16.")
            self.a = a
            self.b = b

        def evaluate(self):
            return [self.a[i] and self.b[i] for i in range(16)]

    class CAVirtualNot16Primitive(CAVirtualChip):
        """A primitive chip that performs a logical NOT operation over 16 bits."""
        def __init__(self, inp):
            if len(inp) != 16:
                raise CAVirtualChipBusError("Not16: Expected input of bus length 16.")
            self.inp = inp

        def evaluate(self):
            return [not i for i in self.inp]

    class CAVirtualOr16Primitive(CAVirtualChip):
        """A primitive chip that performs a logical OR operation over 16 bits."""
        def __init__(self, a, b):
            if len(a) != 16 or len(b) != 16:
                raise CAVirtualChipBusError("Or16: Expected inputs of bus length 16.")
            self.a = a
            self.b = b

        def evaluate(self):
            return [self.a[i] or self.b[i] for i in range(16)]

    class CAVirtualOr8WayPrimitive(CAVirtualChip):
        """A primitive chip that performs a logical OR operation between 8 bits."""
        def __init__(self, inp):
            if len(inp) != 8:
                raise CAVirtualChipBusError("Or8Way: Expected input of bus length 8.")
            self.inp = inp

        def evaluate(self):
            out = self.inp[0]
            for i in range(1, 8):
                out = out or self.inp[i]
            return out

    class CAVirtualMux16Primitive(CAVirtualChip):
        """A primitive chip that performs a selection operation (multiplexer) over 16 bits."""
        def __init__(self, a, b, select):
            if len(a) != 16 or len(b) != 16:
                raise CAVirtualChipBusError("Mux16: Expected inputs of bus length 16.")
            self.a = a
            self.b = b
            self.select = select

        def evaluate(self):
            return [MUX(self.a[i], self.b[i], self.select).evaluate() for i in range(16)]

    class CAVirtualMux4Way16Primitive(CAVirtualChip):
        """A primitive chip that performs a selection operation (multiplexer) between four 16-bit inputs."""
        def __init__(self, a, b, c, d, select):
            if len(a) != 16 or len(b) != 16 or len(c) != 16 or len(d) != 16:
                raise CAVirtualChipBusError("Mux4Way16: Expected inputs of bus length 16.")
            if len(select) != 2:
                raise CAVirtualChipBusError("Mux4Way16: Expected input of bus length 2.")
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.select = select

        def evaluate(self):
            ab = CAVirtualMux16Primitive(self.a, self.b, self.select[0]).evaluate()
            cd = CAVirtualMux16Primitive(self.c, self.d, self.select[0]).evaluate()
            return CAVirtualMux16Primitive(ab, cd, self.select[1]).evaluate()

    class CAVirtualMux8Way16Primitive(CAVirtualChip):
        """A primitive chip that performs a selection operation (multiplexer) between eight 16-bit inputs."""
        def __init__(self, a, b, c, d, e, f, g, h, select):
            if not all([len(x) == 16 for x in [a, b, c, d, e, f, g, h]]):
                raise CAVirtualChipBusError("Mux8Way16: Expected inputs of bus length 16.")
            if len(select) != 3:
                raise CAVirtualChipBusError("Mux4Way16: Expected input of bus length 3.")
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e
            self.f = f
            self.g = g
            self.h = h
            self.select = select

        def evaluate(self):
            ma = CAVirtualMux4Way16Primitive(self.a, self.b, self.c, self.d, self.select[:2]).evaluate()
            mb = CAVirtualMux4Way16Primitive(self.e, self.f, self.g, self.h, self.select[:2]).evaluate()
            return CAVirtualMux16Primitive(ma, mb, self.select[2]).evaluate()

    class CAVirtualDmux4WayPrimitive(CAVirtualChip):
        """A primitive chip that performs a deselect operation (de-multiplexer) between 4 bits."""
        def __init__(self, inp, select):
            if len(select) != 2:
                raise CAVirtualChipBusError("Dmux4Way: Expected input of bus length 2.")
            self.inp = inp
            self.select = select

        def evaluate(self):
            a_in, b_in = DMUX(self.inp, self.select[1])
            a, b = DMUX(a_in, self.select[0])
            c, d = DMUX(b_in, self.select[0])
            return (a, b, c, d)

    class CAVirtualDmux8WayPrimitive(CAVirtualChip):
        """A primitive chip that performs a deselect operation (de-multiplexer) between 8 bits."""
        def __init__(self, inp, select):
            if len(select) != 3:
                raise CAVirtualChipBusError("Dmux8Way: Expected input of bus length 3.")
            self.inp = inp
            self.select = select

        def evaluate(self):
            a_in, b_in = DMUX(self.inp, self.select[2])
            a, b, c, d = CAVirtualDmux4WayPrimitive(a_in, self.select[:2])
            e, f, g, h = CAVirtualDmux4WayPrimitive(b_in, self.select[:2])
            return (a, b, c, d, e, f, g, h)

    AND16 = CAVirtualAnd16Primitive
    NOT16 = CAVirtualNot16Primitive
    MUX16 = CAVirtualMux16Primitive
    OR16 = CAVirtualOr16Primitive
    OR8WAY = CAVirtualOr8WayPrimitive
    MUX4WAY16 = CAVirtualMux4Way16Primitive
    MUX8WAY16 = CAVirtualMux8Way16Primitive
    DMUX4WAY = CAVirtualDmux4WayPrimitive

