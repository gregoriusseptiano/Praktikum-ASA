N, T = map(int, input().split())

lagu = []
for i in range(N):
    d, f = map(int, input().split())
    if d < 5:
        lagu.append((d, f))
if len(lagu) == 0:
    print(0)
    exit()
m = len(lagu)
dp = [[-1] * (m + 1) 
      for i in range(T + 1)]
dp[0][0] = 0
for t in range(T + 1):
    for last in range(m + 1):
        if dp[t][last] != -1:  
            for i in range(1, m + 1):
                if i != last:   
                    durasi, fokus = lagu[i - 1]
                    if t + durasi <= T:
                        nilai = dp[t][last] + fokus
                        if nilai > dp[t + durasi][i]:
                            dp[t + durasi][i] = nilai
jawaban = 0
for t in range(T + 1):
    for last in range(m + 1):
        if dp[t][last] > jawaban:
            jawaban = dp[t][last]

print(jawaban)