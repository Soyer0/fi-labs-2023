from itertools import product
from scipy.stats import norm
from sequence import known_sequence
from multiprocessing import Pool
from base import LFSR

L1_polynom = [3, 0]


def calc_L1(init):
    L1 = LFSR(init, L1_polynom)
    result = bytearray()
    append = result.append
    nxt = L1.next
    [append(nxt()) for _ in range(222)]
    R = sum(result[i] ^ known_sequence[i] for i in range(222))
    if R <= 71:
        return (list(init), R)


if __name__ == '__main__':
    gen = (bytearray(vector) for vector in product([0, 1], repeat=25))
    pool = Pool()
    results = pool.map(calc_L1, gen)
    results = sorted(filter(None, results), key=lambda x: x[1])
    print(results)

# beta = 1 / (2 ** 25)
# t_beta = norm.ppf(1 - beta, loc=0, scale=1)
# t_alpha = norm.ppf(0.99, loc=0, scale=1)
# print(beta)
# print(t_beta)
# print(t_alpha)
# # solve C = n/4+t_alpha*sqrt(3n/16); t_beta = (n/2 - C)/sqrt(n/4)
# C = 71
# N = 222
