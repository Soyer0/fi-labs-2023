class LRZ:
    def __init__(self, filling: bytearray, recurrent: tuple) -> None:
        self.registry = filling
        self.recurrent = recurrent

    def generate(self) -> 0 | 1:
        ret_val = self.registry[0]
        bits_to_xor = [self.registry[bit] for bit in self.recurrent]
        generated = sum(bits_to_xor) % 2
        self.registry.append(generated)
        self.registry.pop(0)
        return ret_val


def generate_geffe(lrz1: LRZ, lrz2: LRZ, lrz3: LRZ) -> 0 | 1:
    x, y, s = lrz1.generate(), lrz2.generate(), lrz3.generate()
    return (s & x) ^ ((1 ^ s) & y)
