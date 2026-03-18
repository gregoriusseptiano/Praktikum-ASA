N, M = map(int, input().split())
data = input().split()

def carikamar(x, F, lantai):
    if x <= F[lantai]:
        hasil = (lantai + 1, x)
    else:
        sisa = x - F[lantai]
        hasil = carikamar(sisa, F, lantai + 1)
    return hasil

def bacaF(data, i, arr):
    if i == len(data):
        hasil = arr
    else:
        hasil = bacaF(data, i + 1, arr + [int(data[i])])
    return hasil

def proses(m, F, i):
    if i < m:
        x = int(input())
        lantai, kamar = carikamar(x, F, 0)
        print(lantai, kamar)
        proses(m, F, i + 1)

F = bacaF(data, 0, [])

proses(M, F, 0)