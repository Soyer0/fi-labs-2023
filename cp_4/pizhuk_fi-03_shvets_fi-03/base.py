class LFSR:
    def __init__(self, initial: bytearray, polynom: list[int]):
        self.sequence = initial.copy()
        self.polynom = polynom

    def next(self):
        seq = self.sequence
        result = seq[0]
        nxt = 0
        for el in self.polynom:
            nxt ^= seq[el]
        del seq[0]
        seq.append(nxt)
        return result


class Geffe:
    def __init__(self, L1: LFSR, L2: LFSR, L3: LFSR):
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3

    def next(self):
        x = self.L1.next()
        y = self.L2.next()
        s = self.L3.next()
        return (s & x) ^ ((1 ^ s) & y)
