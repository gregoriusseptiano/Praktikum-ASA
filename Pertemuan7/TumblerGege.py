N = int(input())
PInput = list(map(int, input().split()))

P = [0] * (N + 1)
def IsiP(i):
    if i <= N:
        P[i] = PInput[i - 1]
        IsiP(i + 1)
IsiP(1)

ans = [0] * (N + 1)
def jalan(current, visited, hasil):
    if visited[current] == 0:
        visited[current] = 1
        jalan(P[current], visited, hasil)
    else:
        hasil[0] = current

def proses(a):
    if a <= N:
        visited = [0] * (N + 1)
        hasil = [0]
        jalan(a, visited, hasil)
        ans[a] = hasil[0]
        proses(a + 1)
proses(1)

def cetak(i):
    if i <= N:
        print(ans[i])
        cetak(i + 1)
cetak(1)