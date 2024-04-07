N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(input()))

add_guard = 0
col = []
row = []

# M이 N보다 큰 경우
for i in range(N):
    if 'X' not in graph[i]:
        row.append(i)

for i in range(M):
    if 'X' not in [graph[n][i] for n in range(N)]:
        col.append(i)
print(max(len(col), len(row)))