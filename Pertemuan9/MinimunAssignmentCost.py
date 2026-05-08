# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026
# Lab : E1

n = int(input())
cost = []
i = 0
while i < n:
    baris = list(map(int, input().split()))
    cost.append(baris)
    i += 1

def HitungBound(pekerja, tugasTerpakai, BiayaSekarang):
    bound = BiayaSekarang
    for i in range(pekerja, n):
        minimum = float("inf")
        for j in range(n):
            if not tugasTerpakai[j] and cost[i][j] < minimum:
                minimum = cost[i][j]
        bound += minimum
    return bound

def AssignmentBranchBound():
    SolusiTerbaik = [float("inf")]
    tugasTerpakai = [False] * n

    def dfs(pekerja, biaya):
        if pekerja == n:
            if biaya < SolusiTerbaik[0]:
                SolusiTerbaik[0] = biaya
        else:
            for j in range(n):
                if not tugasTerpakai[j]:
                    BiayaBaru = biaya + cost[pekerja][j]
                    tugasTerpakai[j] = True
                    bound = HitungBound(pekerja + 1, tugasTerpakai, BiayaBaru)
                    if bound < SolusiTerbaik[0]:
                        dfs(pekerja + 1, BiayaBaru)
                    tugasTerpakai[j] = False

    dfs(0, 0)
    return SolusiTerbaik[0]

print(AssignmentBranchBound())