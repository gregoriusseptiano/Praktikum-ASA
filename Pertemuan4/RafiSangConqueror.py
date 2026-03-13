n, m = map(int, input().split())
a = list(map(int, input().split()))

def cari(a, l, r, x):
    hasil = -1
    if l <= r:
        mid = (l + r) // 2
        if a[mid] >= x:
            kiri = cari(a, l, mid - 1, x)
            if kiri == -1:
                hasil = mid + 1
            else:
                hasil = kiri
        else:
            hasil = cari(a, mid + 1, r, x)

    return hasil

def tanya(a, n, q):
    if q > 0:
        x = int(input())
        h = cari(a, 0, n-1, x)
        print(h)
        tanya(a, n, q-1)

tanya(a, n, m)
