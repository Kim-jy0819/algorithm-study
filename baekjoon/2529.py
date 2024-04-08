N = int(input())
marker_list = input().split()
visited = [0 for _ in range(10)]
result = []
def dfs(depth, number):
    if depth == N:
        result.append(number)
        return
    for i in range(10):
        if visited[i]==0 and eval(f'{number[-1]}{marker_list[depth]}{i}'):
            visited[i] = 1
            dfs(depth+1, number+str(i))
            visited[i] = 0

for i in range(10):
    visited[i] = 1
    dfs(0, f'{i}')
    visited[i] = 0

result = sorted(result)
print(result[-1])
print(result[0])
