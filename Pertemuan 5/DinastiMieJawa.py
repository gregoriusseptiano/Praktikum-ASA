R, C = map(int, input().split())

def baca(data, i, arr):
    if i == len(data):
        hasil = arr
    else:
        hasil = baca(data, i + 1, arr + [int(data[i])])
    return hasil

def cek(arr, kiri, kanan):
    if kiri >= kanan:
        hasil = True
    else:
        if arr[kiri] != arr[kanan]:
            hasil = False
        else:
            hasil = cek(arr, kiri + 1, kanan - 1)
    return hasil

def bacamatriks(r, c, i, arr):
    if i == r:
        hasil = arr
    else:
        baris = input().split()
        angka = baca(baris, 0, [])
        hasil = bacamatriks(r, c, i + 1, arr + angka)
    return hasil

arr = bacamatriks(R, C, 0, [])

total = R * C
rapi = cek(arr, 0, total - 1)

if rapi:
    print("RAPI")
else:
    print("TIDAK")