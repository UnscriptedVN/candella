#
# CAVirtualPlatformChipsetArithmetic.rpy
# Virtual Platform (Candella)
#
# (C) 2021 Marquis Kurt. A/ll rights reserved.
#

init offset = -49
init python in CAVirtualPlatform:
    class CAVirtualHalfAdder(CAVirtualChip):
        """An arithmetic chip that performs a half-add."""
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def evaluate(self):
            a_sum = XOR(self.a, self.b).evaluate()
            a_carry = AND(self.a, self.b).evaluate()
            return a_sum, a_carry

    class CAVirtualFullAdder(CAVirtualChip):
        """An arithmetic chip that adds two bits, with a carry."""
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        def evaluate(self):
            first_sum, first_carry = CAVirtualHalfAdder(self.a, self.b).evaluate()
            total_sum, second_carry = CAVirtualHalfAdder(first_sum, self.c).evaluate()
            total_carry = OR(first_carry, second_carry).evaluate()
            return total_sum, total_carry

    class CAVirtualAdd16(CAVirtualChip):
        """An arithmetic chip that adds 16 bit numbers together."""
        def __init__(self, a, b):
            if len(a) != 16 or len(b) != 16:
                raise CAVirtualChipBusError("Add16: Expected inputs of bus length 16.")
            self.a = a
            self.b = b

        def evaluate(self):
            sums = []
            previous_carry = 0
            for i in range(16):
                new_sum, new_carry = CAVirtualFullAdder(self.a[i], self.b[i], previous_carry).evaluate()
                sums.append(new_sum)
                previous_carry = new_carry
            return sums

    class CAVirtualInc16(CAVirtualChip):
        """An arithmetic chip that increments a 16-bit number by one."""
        def __init__(self, inp):
            if len(inp) != 16:
                raise CAVirtualChipBusError("Inc16: Expected input of bus length 16.")
            self.inp = inp

        def evaluate(self):
            return CAVirtualAdd16(self.inp, [0 for _ in range(15)] + [1]).evaluate()


    class CAVirtualALU(CAVirtualChip):
        """The Candella Arithmetic Logic Unit (ALU). The ALU is responsible for performing multiple arithmetic
            operations on two 16-bit numbers.
        """
        def __init__(self, x, y, zx, nx, zy, ny, f, no):
            if len(x) != 16 or len(y) != 16:
                raise CAVirtualChipBusError("ALU: Expected input of bus length 16.")
            self.x = x
            self.y = y
            self.zx = zx
            self.nx = nx
            self.zy = zy
            self.ny = ny
            self.f = f
            self.no = no

        def evaluate(self):
            not_x = NOT16(self.x).evaluate()
            not_y = NOT16(self.y).evaluate()
            pre_op_x = MUX4WAY16(self.x, [0 for _ in range(16)], not_x, [1 for _ in range(16)],
                [self.zx, self.nx]).evaluate()
            pre_op_y = MUX4WAY16(self.y, [0 for _ in range(16)], not_y, [1 for _ in range(16)],
                [self.zy, self.ny]).evaluate()

            add_xy = CAVirtualAdd16(pre_op_x, pre_op_y).evaluate()
            and_xy = AND16(pre_op_x, pre_op_y).evaluate()
            op = MUX16(and_xy, add_xy, self.f).evaluate()

            nop = NOT16(op).evaluate()
            out = MUX16(op, nop, self.no).evaluate()
            ng  = out[15]
            lsb = out[:8]; msb = out[8:]

            or_lsb = OR8WAY(lsb).evaluate()
            or_msb = OR8WAY(msb).evaluate()
            sig_bits = OR(or_lsb, or_msb).evaluate()
            zr = NOT(sig_bits).evaluate()

            return out, zr, ng

    HALF_ADDER = CAVirtualHalfAdder
    FULL_ADDER = CAVirtualFullAdder
    ADD16 = CAVirtualAdd16
    INC16 = CAVirtualAdd16
    ALU = CAVirtualALU