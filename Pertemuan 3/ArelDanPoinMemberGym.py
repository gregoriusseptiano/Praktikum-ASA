n, k = map(int, input().split())

ops = []
def baca(i):
    if i < n:
        op1, c1, op2, c2 = input().split()
        ops.append((op1, int(c1), op2, int(c2)))
        baca(i + 1)
baca(0)

def hitung(op, c, x):
    if op == '+':
        return x + c
    else:
        return x * c

def cari(hari, poin):
    if hari == n:
        return poin
    else:
        op1, c1, op2, c2 = ops[hari]
        p1 = hitung(op1, c1, poin)
        p2 = hitung(op2, c2, poin)
        a = cari(hari + 1, p1)
        b = cari(hari + 1, p2)

        if a > b:
            return a
        else:
            return b

print(cari(0, k))