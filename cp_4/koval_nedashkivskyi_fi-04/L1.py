def calc_L1(z, queue):

    import numpy as np
    from math import sqrt, floor

    Z = np.zeros(len(z), dtype=int)
    for i in range(len(z)):
        Z[i] = int(z[i])

    n1 = 25
    t_b25 = 5.419983 

    def calc_N(t_b):
        N = (4 *  t_b * sqrt(0.5 * (0.5)) + 4 * 2.326348 * sqrt(0.25 * (0.75))) ** 2
        C = N * 0.25 + 2.326348 * sqrt(N * 0.1875)
        return floor(N), floor(C)

    def calc(n1, N):
        L1 = np.zeros(2 ** n1 + N, dtype=bool)
        L1[n1 - 1] = 1
        for i in range(2 ** n1 + N - 26):
            L1[i + 25] = L1[i] ^ L1[i + 3]
        print(1)
        return L1

    def sieve(L1, N, C, Z):
        candidates = []
        for i in range(2 ** n1):
            x1 = L1[i:i+N]
            R = 0
            for j in range(N):
                if Z[j] != x1[j]:
                    R += 1
            if R < C:
                candidates.append(x1[:n1])
        return candidates
        
    N, C = calc_N(t_b25)
    Z = Z[0:N]
    L1 = calc(n1, N)
    candid = sieve(L1, N, C, Z)
    print("yupie1!")

    file = open("L1.txt", "w+")
    for i in candid:
        file.write(str(i))
        file.write('\n')
    file.close()
    
    queue.put(candid)


