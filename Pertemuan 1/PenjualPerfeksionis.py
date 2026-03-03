n = int(input())
arr = list(map(int, input().split()))

min_val = min(arr)
max_val = max(arr)
min_energy = float('inf')

for target in range (min_val, max_val + 1):
    total = 0
    for value in arr:
        total += abs(value - target)
    min_energy = min(min_energy, total)
        
print(min_energy)
    