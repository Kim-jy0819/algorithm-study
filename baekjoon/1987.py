import copy
from collections import deque
R, C = map(int, input().split())

graph = []
visited = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(R):
    graph.append(list(input()))



dr = [0,0,1,-1]
dc = [1,-1,0,0]
alphabet_list = [0 for _ in range(26)]
maximum = 0
def dfs(r, c, alphabet_list, depth):
    global maximum
    maximum = max(maximum, depth)

    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if next_r not in range(R) or next_c not in range(C):
            continue
        alphabet = graph[next_r][next_c]
        if alphabet_list[ord(alphabet) - 65]:
            continue
        alphabet_list[ord(alphabet) - 65] = True
        dfs(next_r, next_c, alphabet_list, depth+1)
        alphabet_list[ord(alphabet) - 65] = False

alphabet_list[ord(graph[0][0]) - 65] = True
dfs(0,0,alphabet_list, 1)

print(maximum)