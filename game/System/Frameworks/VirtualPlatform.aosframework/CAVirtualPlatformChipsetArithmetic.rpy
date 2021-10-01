#
# CAVirtualPlatformChipsetArithmetic.rpy
# Virtual Platform (Candella)
#
# (C) 2021 Marquis Kurt. A/ll rights reserved.
#

init offset = -49
init python in CAVirtualPlatform:
    class CAVirtualHalfAdder(CAVirtualChip):
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def evaluate(self):
            a_sum = XOR(self.a, self.b).evaluate()
            a_carry = AND(self.a, self.b).evaluate()
            return a_sum, a_carry

    class CAVirtualFullAdder(CAVirtualChip):
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
        def __init__(self, inp):
            if len(inp) != 16:
                raise CAVirtualChipBusError("Inc16: Expected input of bus length 16.")
            self.inp = inp

        def evaluate(self):
            return CAVirtualAdd16(self.inp, [0 for _ in range(15)] + [1]).evaluate()