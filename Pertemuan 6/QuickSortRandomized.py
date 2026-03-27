import random

n = int(input())
arr = list(map(int, input().split()))

def Partisi(arr, i, j):
    pivot = arr[j]
    p = i - 1
    while i < j:
        if arr[i] <= pivot:
            p = p + 1
            temp = arr[p]
            arr[p] = arr[i]
            arr[i] = temp
            
        i = i + 1

    temp = arr[p+1]
    arr[p+1] = arr[j]
    arr[j] = temp

    return p + 1

def QuickSort(arr, i, j):
    if i < j:
        PivotIndex = Partisi(arr, i, j)
        QuickSort(arr, i, PivotIndex - 1)
        QuickSort(arr, PivotIndex + 1, j)

def PrintArray(arr, idx, n):
    if idx == n:
        return 0
    print(arr[idx], end = " ")
    PrintArray(arr, idx + 1, n)

QuickSort(arr, 0, n - 1)
PrintArray(arr, 0, n)