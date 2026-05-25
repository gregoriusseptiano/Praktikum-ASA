# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026
# Lab : E1

import sys
sys.setrecursionlimit(100000)
INF = float('inf')

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    antrean = []
    for i in range(N):
        antrean.append(int(data[idx+i]))
    idx += N
    
    jarak = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(int(data[idx+j]))
        jarak.append(row)
        idx += N

    memo = {}
    def dfs(pos, mask):
        if mask == (1 << N) - 1:
            return jarak[pos][0]
        if (pos, mask) in memo:
            return memo[(pos, mask)]

        k = bin(mask).count('1')
        best = INF
        for v in range(1, N):
            if not (mask >> v & 1):
                cost = jarak[pos][v] + k * antrean[v]
                best = min(best, cost + dfs(v, mask | (1 << v)))

        memo[(pos, mask)] = best
        return best

    print(dfs(0, 1))
solve()