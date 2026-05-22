# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026
# Lab : E1

n = int(input())

if n <= 1:
    print(n)
else:
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    i = 2
    while i <= n:
        dp[i] = dp[i - 1] + dp[i - 2]
        i = i + 1
    print(dp[n])