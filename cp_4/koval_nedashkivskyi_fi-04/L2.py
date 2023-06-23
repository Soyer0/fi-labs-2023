def calc_L2(z, queue):

    import numpy as np
    from math import sqrt, floor

    Z = np.zeros(len(z), dtype=int)
    for i in range(len(z)):
        Z[i] = int(z[i])

    n2 = 26
    t_b26 = 5.542594

    def calc_N(t_b):
        N = (4 *  t_b * sqrt(0.5 * (0.5)) + 4 * 2.326348 * sqrt(0.25 * (0.75))) ** 2
        C = N * 0.25 + 2.326348 * sqrt(N * 0.1875)
        return floor(N), floor(C)

    def calc(n2, N):
        L2 = np.zeros(2 ** n2 + N, dtype=bool)
        L2[n2 - 1] = 1
        for i in range(2 ** n2 + N - 26):
            L2[i + 26] = L2[i] ^ L2[i + 1] ^ L2[i + 2] ^ L2[i + 6] 
        print(2)
        return L2

    def sieve(L2, N, C, Z):
        candidates = []
        for i in range(2 ** n2):
            x1 = L2[i:i+N]
            R = 0
            for j in range(N):
                if Z[j] != x1[j]:
                    R += 1
            if R < C:
                candidates.append(x1[:n2])
        return candidates
        
    N, C = calc_N(t_b26)
    Z = Z[0:N]
    L2 = calc(n2, N)
    candid = sieve(L2, N, C, Z)
    print("yupie2!")

    file = open("L2.txt", "w+")
    for i in candid:
        file.write(str(i))
        file.write('\n')
    file.close()
    
    queue.put(candid)

