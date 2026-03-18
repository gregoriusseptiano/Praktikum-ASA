N, K = map(int, input().split())
G = list(map(int, input().split()))

def cari(i, total):
    if i == N:
        if total <= K:
            return total
        else:
            return 0
    else:
        a = cari(i + 1, total)
        b = 0
        if total + G[i] <= K:
            b = cari(i + 1, total + G[i])
        
        if a > b:
            return a
        else:
            return b

hasil = cari(0, 0)
print(hasil)