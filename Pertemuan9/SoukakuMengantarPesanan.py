# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026
# Lab : E1

n = int(input())
jarak = []
i = 0
while i < n:
    baris = list(map(int, input().split()))
    jarak.append(baris)
    i += 1
awal = 0

def HitungBound(visited, BiayaSekarang):
    bound = BiayaSekarang
    for i in range(n):
        if not visited[i]:
            minimum = float("inf")
            for j in range(n):
                if i != j and jarak[i][j] < minimum:
                    minimum = jarak[i][j]
            bound += minimum
    return bound

def TSPBranchBound():
    SolusiTerbaik = [float("inf")]
    RuteTerbaik   = [[]]
    visited = [False] * n
    visited[awal] = True

    def dfs(posisi, visited, rute, biaya):
        if len(rute) == n:
            total = biaya + jarak[posisi][awal]
            if total < SolusiTerbaik[0]:
                SolusiTerbaik[0] = total
                RuteTerbaik[0] = rute + [awal]
        else:
            for i in range(n):
                if not visited[i]:
                    BiayaBaru = biaya + jarak[posisi][i]
                    bound = HitungBound(visited, BiayaBaru)
                    if bound < SolusiTerbaik[0]:
                        visited[i] = True
                        dfs(i, visited, rute + [i], BiayaBaru)
                        visited[i] = False
                        
    dfs(awal, visited, [awal], 0)
    return RuteTerbaik[0], SolusiTerbaik[0]

rute, total = TSPBranchBound()
print(total)