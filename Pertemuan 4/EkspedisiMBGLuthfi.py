n = int(input())
arr = list(map(int, input().split()))

def cari(arr, i, r):
    if i == r:
        return arr[i], arr[i]
    if r == i + 1:
        if arr[i] < arr[r]:
            return arr[i], arr[r]
        else:
            return arr[r], arr[i]

    mid = (i + r) // 2
    a1, b1 = cari(arr, i, mid)
    a2, b2 = cari(arr, mid + 1, r)
    
    if a1 < a2:
        a = a1
    else:
        a = a2
    if b1 > b2:
        b = b1
    else: 
        b = b2
        
    return a,b 

a,b = cari(arr, 0, n-1)
print(a,b)