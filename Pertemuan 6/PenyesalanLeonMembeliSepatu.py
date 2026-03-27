n = int(input())
data = list(map(int, input().split()))
target = int(input())

def QuickSort(arr, kiri, kanan):
    jumlah = 1
    if kiri < kanan:
        posisi = bagi(arr, kiri, kanan)
        kiriHitung = QuickSort(arr, kiri, posisi - 1)
        kananHitung = QuickSort(arr, posisi + 1, kanan)
        jumlah = jumlah + kiriHitung + kananHitung

    hasil = jumlah
    return hasil

def bagi(arr, kiri, kanan):
    pivot = arr[kanan]
    i = kiri - 1
    j = kiri
    while j < kanan:
        if arr[j] <= pivot:
            i = i + 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        
        j = j + 1

    temp = arr[i + 1]
    arr[i + 1] = arr[kanan]
    arr[kanan] = temp

    hasil = i + 1
    return hasil

i = 0
jumlahCocok = 0

while i < n:
    arr = [0] * n
    j = 0
    while j < n:
        arr[j] = data[j]
        j = j + 1

    temp = arr[i]
    arr[i] = arr[n - 1]
    arr[n - 1] = temp
    hitung = QuickSort(arr, 0, n - 1)

    if hitung == target:
        jumlahCocok = jumlahCocok + 1

    i = i + 1

print(jumlahCocok)