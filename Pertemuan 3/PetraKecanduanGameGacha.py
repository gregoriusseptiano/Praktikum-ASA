N, X = map(int, input().split())

mesin = []
def baca(i):
    if i < N:
        t1, t2 = map(int, input().split())
        mesin.append((t1, t2))
        baca(i + 1)
baca(0)

def simulasi(p, ssr, T):
    if p >= T - 1:
        return 0, ssr + 1
    else:
        return p + 1, ssr

def cari(i, p, ssr):
    if ssr >= X:
        return i
    elif i == N:
        return 10**18
    else:
        t1, t2 = mesin[i]
        p1, s1 = simulasi(p, ssr, t1)
        p2, s2 = simulasi(p, ssr, t2)
        a = cari(i + 1, p1, s1)
        b = cari(i + 1, p2, s2)

        if a < b:
            return a
        else:
            return b

hasil = cari(0, 0, 0)
if hasil > N:
    print(-1)
else:
    print(hasil)