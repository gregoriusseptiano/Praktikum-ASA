# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026
# Lab : E1

import heapq

N, M = map(int, input().split())
S, G = map(int, input().split())

graph = {}
for i in range(1, N + 1):
    graph[i] = []
for j in range(M):
    parts = input().split()
    u = int(parts[0])
    v = int(parts[1])
    w = int(parts[2])
    graph[u].append((v, w))
    graph[v].append((u, w))

h = list(map(int, input().split()))
heuristik = {}
for i in range(N):
    heuristik[i + 1] = h[i]

def GreedyBFS():
    OpenList = [(heuristik[S], S, 0, [S])]
    inOpen   = {S}
    expanded = []                             

    while OpenList:
        h_now, node, cost, rute = heapq.heappop(OpenList)
        expanded.append(node)                
        if node == G:
            return rute, cost, expanded

        for tetangga, bobot in graph[node]:
            if tetangga not in inOpen:         
                heapq.heappush(OpenList, (heuristik[tetangga], tetangga, cost + bobot, rute + [tetangga]))
                inOpen.add(tetangga)

    return None, 0, []

rute, cost, expanded = GreedyBFS()
print("Path: " + " ".join(str(k) for k in rute))
print("Cost: " + str(cost))
print("Expanded: " + " ".join(str(k) for k in expanded))