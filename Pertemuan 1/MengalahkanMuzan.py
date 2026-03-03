n = int(input())

A = list(map(int, input().split()))

C = []

for _ in range(n):

    C.append(list(map(int, input().split())))

visited = [False] * n

min_total = 10**18

def dfs(count, last, total):

    global min_total

    if count == n:

        if total < min_total:

            min_total = total

        return

    for i in range(n):

        if not visited[i]:

            visited[i] = True

            if last == -1:

                new_total = total + A[i]

            else:

                new_total = total + A[i] + C[i][last]

            dfs(count + 1, i, new_total)

            visited[i] = False

dfs(0, -1, 0)

print(min_total)