from L2_results import results as l2_results
from L1_results import results as l1_results
from base import LFSR, Geffe
from sequence import known_sequence
from itertools import product
from multiprocessing import Pool

L1_polynom = [3, 0]
L2_polynom = [6, 2, 1, 0]
L3_polynom = [5, 2, 1, 0]


def calc_L3(init):
    L3 = LFSR(init, L3_polynom)
    for l1_input in l1_results:
        L1 = LFSR(l1_input[0], L1_polynom)
        for l2_input in l2_results:
            L2 = LFSR(l2_input[0], L2_polynom)
            geffe = Geffe(L1=L1, L2=L2, L3=L3)
            for i in range(len(known_sequence)):
                if known_sequence[i] != geffe.next():
                    return
            print(f'FINISHED: L1={l1_input[0]}, L2={l2_input[0]}, L3={init}')
            return (l1_input, l2_input, init)


if __name__ == '__main__':
    gen = (bytearray(vector) for vector in product([0, 1], repeat=27))
    pool = Pool(1)
    results = pool.map(calc_L3, gen)
    results = list(filter(None, results))
    print(results)
