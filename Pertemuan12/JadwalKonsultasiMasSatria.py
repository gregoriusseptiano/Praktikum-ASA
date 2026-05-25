# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026
# Lab : E1

import sys

def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def solve():
    InputData = sys.stdin.read().split()
    idx = 0
    n = int(InputData[idx])
    idx += 1
    
    consultations = []
    i = 0
    while i < n:
        s = int(InputData[idx])
        idx += 1
        e = int(InputData[idx])
        idx += 1
        consultations.append((e, s))
        i += 1
    
    consultations = MergeSort(consultations)  
    count = 0
    LastEnd = -1
    i = 0
    while i < n:
        e, s = consultations[i]
        if s >= LastEnd:
            count += 1
            LastEnd = e
        i += 1
    
    print(count)
solve()