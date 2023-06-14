from lrz import LRZ, generate_geffe
from variant import generated
from constants import N1, N2, C1, C2
from multiprocessing import Pool
from itertools import product
from functools import partial

l1_recurrent = (3, 0)
l2_recurrent = (6, 2, 1, 0)
l3_recurrent = (5, 2, 1, 0)


def calculate_lrz(filling: bytes, recurrent: tuple, N: int, C: int):
    lrz = LRZ(bytearray(filling), recurrent)
    generated_vector = bytearray()
    for i in range(N):
        generated_vector.append(lrz.generate())
    r = 0
    for i in range(N):
        r += generated_vector[i] != generated[i]
    if r <= C:
        return filling, r


def calculate_final(filling: bytes, l1_results: list, l2_results: list):
    l3 = LRZ(bytearray(filling), l3_recurrent)
    for l1_filling in l1_results:
        l1 = LRZ(bytearray(l1_filling[0]), l1_recurrent)
        for l2_filling in l2_results:
            l2 = LRZ(bytearray(l2_filling[0]), l2_recurrent)
            for i in range(len(generated)):
                if generated[i] != generate_geffe(l1, l2, l3):
                    return
            print(f'Result: {l1_filling[0]=}, {l2_filling[0]=}, l3_filling={filling}')


def clean_results(results: list) -> list:
    filtered_results = filter(None, results)
    sorted_results = sorted(filtered_results, key=lambda x: x[1])
    print(sorted_results)
    return sorted_results


if __name__ == '__main__':
    l1_vectors = (bytes(binary) for binary in product([0, 1], repeat=25))
    l2_vectors = (bytes(binary) for binary in product([0, 1], repeat=26))
    l3_vectors = (bytes(binary) for binary in product([0, 1], repeat=27))
    pool = Pool()
    l1_results = pool.map(partial(calculate_lrz, recurrent=l1_recurrent, N=N1, C=C1), l1_vectors)
    print('FINISHED L1')
    l2_results = pool.map(partial(calculate_lrz, recurrent=l2_recurrent, N=N2, C=C2), l2_vectors)
    print('FINISHED L2')
    print('L1 RESULTS:')
    l1_results = clean_results(l1_results)
    print('L2 RESULTS:')
    l2_results = clean_results(l2_results)
    pool.map(partial(calculate_final, l1_results=l1_results, l2_results=l2_results), l3_vectors)


a=4
b=5
print(a+b)