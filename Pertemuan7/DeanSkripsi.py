T = int(input())

t = 0
while t < T:
    t += 1

    N, M, S = map(int, input().split())
    graph = [[] for i in range(N + 1)]
    i = 0
    while i < M:
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        i += 1

    dist = [-1] * (N + 1)
    queue = [0] * (N + 5)
    front = 0
    rear = 0
    queue[rear] = S
    rear += 1
    dist[S] = 0

    while front < rear:
        u = queue[front]
        front += 1

        idx = 0
        while idx < len(graph[u]):
            v = graph[u][idx]
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue[rear] = v
                rear += 1
            idx += 1

    BestNode = S
    BestDist = 0

    i = 1
    while i <= N:
        if dist[i] > BestDist:
            BestDist = dist[i]
            BestNode = i
        elif dist[i] == BestDist:
            if i < BestNode:
                BestNode = i
        i += 1

    print(BestNode, BestDist)