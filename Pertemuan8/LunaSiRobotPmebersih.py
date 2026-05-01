# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026
# Lab : E1

import heapq
n, m = map(int, input().split())

h_input = list(map(int, input().split()))
h = [0] * (n + 1)

i = 1
while i <= n:
    h[i] = h_input[i - 1]
    i += 1

graph = {}
i = 1
while i <= n:
    graph[i] = []
    i += 1

i = 0
while i < m:
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    i += 1

start, goal = map(int, input().split())
INF = float('inf')
g = {}

i = 1
while i <= n:
    g[i] = INF
    i += 1

g[start] = 0
pq = []
heapq.heappush(pq, (g[start] + h[start], start))

while len(pq) > 0:
    f_now, node = heapq.heappop(pq)
    if f_now == g[node] + h[node]:
        neighbors = graph[node]
        j = 0
        while j < len(neighbors):
            neighbor, cost = neighbors[j]
            new_g = g[node] + cost
            if new_g < g[neighbor]:
                g[neighbor] = new_g
                f_neighbor = new_g + h[neighbor]
                heapq.heappush(pq, (f_neighbor, neighbor))

            j += 1

if g[goal] == INF:
    print(-1)
else:
    print(g[goal])
