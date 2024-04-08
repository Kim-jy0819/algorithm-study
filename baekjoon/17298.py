N = int(input())

A = list(map(int, input().split()))
stack = [0]
NGE = [-1 for _ in range(N)]

for i in range(1, N):
    while stack and A[i] > A[stack[-1]]:
        NGE[stack.pop()] = A[i]
    stack.append(i)
print(*NGE)
