n = int(input())
a = list(map(int, input().split()))

def hitung(a, l, r):
    if l == r:
        return [a[l]], 0

    mid = (l + r) // 2
    kiri, e1 = hitung(a, l, mid)
    kanan, e2 = hitung(a, mid + 1, r)
    i, j, k = 0, 0, 0
    gabung = [0] * (r - l + 1)
    error = e1 + e2

    while i < len(kiri) and j < len(kanan):
        if kiri[i] <= kanan[j]:
            gabung[k] = kiri[i]
            i += 1
        else:
            gabung[k] = kanan[j]
            error += len(kiri) - i
            j += 1
        k += 1
    while i < len(kiri):
        gabung[k] = kiri[i]
        i += 1
        k += 1
    while j < len(kanan):
        gabung[k] = kanan[j]
        j += 1
        k += 1
    return gabung, error

hasil, error = hitung(a, 0, n-1)

print(error)