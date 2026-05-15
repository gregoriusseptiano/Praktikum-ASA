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
for j in range(M):
    u, v = input().split()
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

awal, tujuan = input().split()
for nama in heuristik:
    if nama not in graph:
        graph[nama] = []

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

    while OpenList:
        h, node, rute = AmbilTerkecil(OpenList)
        inOpen.discard(node)
        if node == tujuan:
            return rute
        visited.append(node)

        for tetangga in graph[node]:
            if tetangga not in visited and tetangga not in inOpen:
                OpenList.append((heuristik[tetangga], tetangga, rute + [tetangga]))
                inOpen.add(tetangga)

    return None

rute = GreedyBFS()

if rute is None:
    print("TIDAK ADA")
else:
    print(" -> ".join(rute))