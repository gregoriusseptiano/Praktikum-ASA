# Nama : Gregorius Septiano Ariadi
# NIM : 24060124120026
# Lab : E1

n, a, b = map(int, input().split())

if n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    dp = [0] * (n + 1)
    dp[0] = a
    dp[1] = b
    i = 2
    while i <= n:
        dp[i] = dp[i - 1] + dp[i - 2]
        i = i + 1
    print(dp[n])