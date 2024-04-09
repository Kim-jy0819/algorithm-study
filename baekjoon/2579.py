N = int(input())
INF = 1e9
dp = [0 for _ in range(N+2)]
dc = [1 for _ in range(N+2)]
step_scores = [0]
for _ in range(N):
    step_scores.append(int(input()))

dp[1] = step_scores[1]
if N >= 3:
    dp[2] = step_scores[1] + step_scores[2]
    pprev = dp[1] + step_scores[3]
    prev = step_scores[2] + step_scores[3]
    if prev > pprev:
        dc[4] = 1
        dp[3] = prev
    else:
        dp[3] = pprev
elif N>= 2:
    dp[2] = step_scores[1] + step_scores[2]
    dc[3] = 0

for i in range(3,N+1):
    if dc[i]:
        prev = dp[i - 1] + step_scores[i]
    else:
        prev = dp[i - 1]
    pprev = dp[i - 2] + step_scores[i]

    if prev > pprev:
        dp[i] = prev
        dc[i+1] = 0
    else:
        dp[i] = pprev
        dc[i+1] = 1

print(dp[N])