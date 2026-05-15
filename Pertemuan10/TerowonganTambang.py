# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026
# Lab : E1

N, M = map(int, input().split())

heuristik = {}
for i in range(N):
    parts = input().split()
    nama = parts[0]
    h = int(parts[1])
    heuristik[nama] = h

graph = {}
for nama in heuristik:
    graph[nama] = []
for j in range(M):
    u, v = input().split()
    graph[u].append(v)

awal, tujuan = input().split()
def AmbilTerkecil(OpenList):
    minimum = 0
    for i in range(len(OpenList)):
        if OpenList[i][0] < OpenList[minimum][0]:
            minimum = i
    return OpenList.pop(minimum)

def GreedyBFS():
    OpenList = [(heuristik[awal], awal, [awal])]
    visited   = []
    inOpen   = {awal}
    diperiksa = 0

    while OpenList:
        h, node, rute = AmbilTerkecil(OpenList)
        inOpen.discard(node)
        diperiksa = diperiksa + 1

        if node == tujuan:
            return rute, diperiksa
        visited.append(node)

        for tetangga in graph[node]:
            if tetangga not in visited and tetangga not in inOpen:
                OpenList.append((heuristik[tetangga], tetangga, rute + [tetangga]))
                inOpen.add(tetangga)

    return None, diperiksa

rute, diperiksa = GreedyBFS()
if rute is None:
    print("TIDAK ADA")
else:
    print(" -> ".join(rute))
    
print("DIPERIKSA: " + str(diperiksa))