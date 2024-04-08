N = int(input())

INF = 1e9
dp = [INF for _ in range(5001)]
dp[3] = 1
dp[5] = 1

for i in range(6, N+1):
    dp[i] = min(dp[i-3]+1, dp[i])
    dp[i] = min(dp[i-5]+1, dp[i])

if dp[N] == INF:
    print(-1)
else:
    print(dp[N])