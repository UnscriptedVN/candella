#
# CAVirtualPlatformChipsetPrimitives.rpy
# Virtual Platform (Candella)
#
# (C) 2021 Marquis Kurt. A/ll rights reserved.
#

init offset = -50
init python in CAVirtualPlatform:
    from abc import ABCMeta, abstractmethod

    class CAVirtualChipBusError(Exception):
        """The length of the specified bus is invalid."""

    class CAVirtualChip:
        __metaclass__ = ABCMeta
        """An abstract class that represents a virtual chip in CAVirtualPlatform."""
        @abstractmethod
        def evaluate(self):
            pass

    class CAVirtualNandPrimitive(CAVirtualChip):
        """A primitive chip that performs a logical NAND operation."""
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def evaluate():
            return not self.a and not self.b

    class CAVirtualNotPrimitive(CAVirtualChip):
        """A primitive chip that performs a logical NOT operation."""
        def __init__(self, inp):
            self.inp = inp

        def evaluate(self):
            return not self.inp

    class CAVirtualAndPrimitive(CAVirtualChip):
        """A primitive chip that performs a logical AND operation."""
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def evaluate(self):
            return not CAVirtualNandPrimitive(self.a, self.b)

    class CAVirtualOrPrimitive(CAVirtualChip):
        """A primitive chip that performs a logical OR operation."""
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def evaluate(self):
            return self.a or self.b

    class CAVirtualXorPrimitive(CAVirtualChip):
        """A primitive chip that performs a logical XOR operation."""
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def evaluate(self):
            return self.a ^ self.b

    class CAVirtualMuxPrimitive(CAVirtualChip):
        """A primitive chip that performs a select operation (multiplexer)."""
        def __init__(self, a, b, select):
            self.a = a
            self.b = b
            self.select = select

        def evaluate(self):
            return self.b if self.select else self.a

    class CAVirtualDmuxPrimitive(CAVirtualChip):
        """A primitive chip that performs a de-select operation (de-multiplexer)."""
        def __init__(self, inp, select):
            self.inp = inp
            self.select = select

        def evaluate(self):
            invert_select = not self.select
            return (self.inp and invert_select, self.select and self.inp)

    NAND = CAVirtualNandPrimitive
    NOT = CAVirtualNotPrimitive
    AND = CAVirtualAndPrimitive
    OR = CAVirtualOrPrimitive
    XOR = CAVirtualXorPrimitive
    MUX = CAVirtualMuxPrimitive
    DMUX = CAVirtualDmuxPrimitive