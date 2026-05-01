# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026
# Lab : E1

import heapq
n, m = map(int, input().split())

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

start, end = map(int, input().split())
INF = float('inf')
dist = {}

i = 1
while i <= n:
    dist[i] = INF
    i += 1

dist[start] = 0
pq = [(0, start)]

while len(pq) > 0:
    current_dist, node = heapq.heappop(pq)
    if current_dist <= dist[node]:
        neighbors = graph[node]
        j = 0
        while j < len(neighbors):
            neighbor, weight = neighbors[j]
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

            j += 1

if dist[end] == INF:
    print(-1)
else:
    print(dist[end])
