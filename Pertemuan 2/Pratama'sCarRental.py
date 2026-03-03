N, M, X = map(int, input().split())

P = []
V = []
C = []
for i in range(N):
    p, v, c = map(int, input().split())
    P.append(p)
    V.append(v)
    C.append(c)
jawaban = 10**18
for mask in range(1 << N):
    totalP = 0
    totalV = 0
    totalC = 0
    for i in range(N):
        if (mask & (1 << i)) != 0:
            totalP += P[i]
            totalV += V[i]
            totalC += C[i]
    if totalP >= M and totalV >= X:
        if totalC < jawaban:
            jawaban = totalC
if jawaban == 10**18:
    print(-1)   
else:
    print(jawaban)