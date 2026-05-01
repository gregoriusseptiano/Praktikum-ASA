# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026
# Lab : E1

n, target = map(int, input().split())
arr = list(map(int, input().split()))

found = [False]  

def backtrack(i, current_sum):
    if not found[0]:  
        if current_sum == target:
            found[0] = True
        else:
            if i < n and current_sum <= target:
                backtrack(i + 1, current_sum + arr[i])
                backtrack(i + 1, current_sum)

backtrack(0, 0)

if found[0]:
    print("YES")
else:
    print("NO")



