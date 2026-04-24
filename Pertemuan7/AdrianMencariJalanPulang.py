N, M, S = map(int, input().split())
graph = [[0] * (N + 1)] * (N + 1)

def FixMatrix(i):
    if i <= N:
        graph[i] = [0] * (N + 1)
        FixMatrix(i + 1)
FixMatrix(0)

visited = [0] * (N + 1)
found = [0]
def InputEdge(i):
    if i < M:
        A, B = map(int, input().split())
        graph[A][B] = 1
        InputEdge(i + 1)

def dfs(u):
    CekTetangga(u, 1)
def CekTetangga(u, v):
    if v <= N:
        if graph[u][v] == 1:
            if v == S and visited[v] == 1:
                found[0] = 1

            if visited[v] == 0:
                visited[v] = 1
                dfs(v)
        CekTetangga(u, v + 1)

visited[S] = 1
InputEdge(0)
dfs(S)

if found[0] == 1:
    print("YES")
else:
    print("NO")