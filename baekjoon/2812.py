# 4 2 (1 ≤ K < N ≤ 500,000)
# 1924
# 94

# 7 3
# 1 3 2 5 1 2 3
# 7 5
# if n - i + 1 <= n - k - count  참고할 남은 개수 >= 채워야할 개수
N, K = map(int, input().split())
numbers = input()

from collections import deque

stack = deque([numbers[0]])
count = 1
for i in range(1, N):
    while (N - i - 1 >= N - K - count) and stack:
        # print(i, N-i-1, N-K-count, stack)
        if stack[-1] < numbers[i]:
            stack.pop()
            count -= 1
        else:
            break
    stack.append(numbers[i])
    count += 1
print(''.join(list(stack)[:N-K]))