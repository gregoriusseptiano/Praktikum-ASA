# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026
# Lab : E1

def solve():
    N, W = map(int, input().split())
    items = []
    i = 0
    while i < N:
        parts = input().split()
        berat = int(parts[0])
        nilai = int(parts[1])
        kategori = int(parts[2])
        items.append((berat, nilai, kategori))
        i += 1

    best = {}
    queue = [(0, W, False, 0)]
    head = 0
    result = 0

    while head < len(queue):
        idx, sisa, AdaWajib, TotalNilai = queue[head]
        head += 1
        if idx == N:
            if AdaWajib and TotalNilai > result:
                result = TotalNilai
        else:
            berat, nilai, kategori = items[idx]
            for ambil in [False, True]:
                if ambil and sisa < berat:
                    continue
                if ambil:
                    NextSisa = sisa - berat
                    NextWajib = AdaWajib or (kategori == 1)
                    NextNilai = TotalNilai + nilai
                else:
                    NextSisa = sisa
                    NextWajib = AdaWajib
                    NextNilai = TotalNilai
                state = (idx + 1, NextSisa, NextWajib)
                if state in best and best[state] >= NextNilai:
                    continue
                best[state] = NextNilai
                queue.append((idx + 1, NextSisa, NextWajib, NextNilai))

    print(result)
solve()