N, M = map(int, input().split())

def hitung(energi, sarang, i):
    if i == len(sarang):
        hasil = 0
    else:
        if sarang[i] <= energi:
            hasil = 1 + hitung(energi, sarang, i + 1)
        else:
            hasil = hitung(energi, sarang, i + 1)
    return hasil

def proses(hari, sarang, energi, i):
    if i == len(energi):
        hasil = 0
    else:
        dapat = hitung(energi[i], sarang, 0)
        hasil = dapat + proses(hari, sarang, energi, i + 1)
    return hasil

def baca(data, i, arr):
    if i == len(data):
        hasil = arr
    else:
        hasil = baca(data, i + 1, arr + [int(data[i])])
    return hasil

sarang = baca(input().split(), 0, [])
energi = baca(input().split(), 0, [])

total = proses(M, sarang, energi, 0)

print(total)