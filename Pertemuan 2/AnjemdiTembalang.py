n = int(input())

matrix = []
i = 0
while i < n:
    row = list(map(int, input().split()))
    matrix.append(row)
    i += 1

labels = []
i = 0
while i < n:
    labels.append(chr(ord('A') + i))
    i += 1
    
visited = [False] * n
visited[0] = True  
best_distance = 10**9
best_path = []

def tsp(current, count, total, path):
    global best_distance, best_path
    if count == n:
        total_akhir = total + matrix[current][0]
        if total_akhir < best_distance:
            best_distance = total_akhir
            best_path = path + [0]
    else:
        i = 1
        while i < n:
            if not visited[i]:
                visited[i] = True
                tsp(i, count + 1, total + matrix[current][i], path + [i])
                visited[i] = False
            i += 1

tsp(0, 1, 0, [0])
print(best_distance)

i = 0
while i < len(best_path):
    print(labels[best_path[i]], end=" ")
    i += 1