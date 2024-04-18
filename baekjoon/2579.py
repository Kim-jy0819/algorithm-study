N = int(input())
dp = [0 for _ in range(301)]
step_scores = [0 for _ in range(301)]
for i in range(1,N+1):
    step_scores[i] = int(input())

dp[1] = step_scores[1]
dp[2] = step_scores[1] + step_scores[2]
dp[3] = max(step_scores[1] + step_scores[3], step_scores[2] + step_scores[3])

for i in range(4, N+1):
    dp[i] = max(dp[i-3] + step_scores[i-1] + step_scores[i], dp[i-2] + step_scores[i])

print(dp[N])