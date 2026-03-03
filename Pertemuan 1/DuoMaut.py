n = int(input())
arr = list(map(int, input().split()))

max_sum = 0

for i in range (n):
    for j in range (i+1, n):
        total = arr[i] + arr [j]
        if total > max_sum:
           max_sum = total
        
print(max_sum)
    