# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026
# Lab : E1

n, t = map(int, input().split())

materi = []
i = 0
while i < n:
    waktu, kepentingan, kesulitan, latihan = map(int, input().split())
    nilai = (kepentingan * 10) + (latihan * 5) - (kesulitan * 2)
    materi.append((waktu, nilai))
    i += 1

dp = [0] * (t + 1)

for waktu, nilai in materi:
    j = t
    while j >= waktu:
        dp[j] = max(dp[j], dp[j - waktu] + nilai)
        j -= 1

print(dp[t])