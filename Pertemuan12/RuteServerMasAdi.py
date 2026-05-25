# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026
# Lab : E1

import heapq

def solve():
    n, m = map(int, input().split())
    adj = []
    i = 0
    while i <= n:
        adj.append([])
        i += 1
    i = 0
    while i < m:
        u, v, w = map(int, input().split())
        adj[u].append((w, v))
        adj[v].append((w, u))
        i += 1

    s, t = map(int, input().split())
    INF = float('inf')
    dist = []
    i = 0
    while i <= n:
        dist.append(INF)
        i += 1
    dist[s] = 0

    def h(node):
        return 0  
    heap = [(0 + h(s), 0, s)]  
    found = False

    while heap and not found:
        f, g, node = heapq.heappop(heap)  
        if g <= dist[node]:
            if node == t:
                found = True
            else:
                j = 0
                neighbors = adj[node]
                while j < len(neighbors):
                    w, nxt = neighbors[j]
                    new_g = g + w
                    new_f = new_g + h(nxt)  
                    if new_g < dist[nxt]:
                        dist[nxt] = new_g
                        heapq.heappush(heap, (new_f, new_g, nxt))
                    j += 1

    if dist[t] != INF:
        print(dist[t])
    else:
        print(-1)

solve()