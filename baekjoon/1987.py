import copy
from collections import deque
R, C = map(int, input().split())

graph = []
for _ in range(R):
    graph.append(list(input()))



dr = [0,0,1,-1]
dc = [1,-1,0,0]
maximum = 0
# alphabet_list = [0 for _ in range(26)]
# def dfs(r, c, depth):
#     global maximum
#     maximum = max(maximum, depth)
#
#     for i in range(4):
#         next_r = r + dr[i]
#         next_c = c + dc[i]
#         if next_r not in range(R) or next_c not in range(C):
#             continue
#         alphabet = graph[next_r][next_c]
#         if alphabet_list[ord(alphabet) - 65]:
#             continue
#         alphabet_list[ord(alphabet) - 65] = True
#         dfs(next_r, next_c, depth+1)
#         alphabet_list[ord(alphabet) - 65] = False
#
# alphabet_list[ord(graph[0][0]) - 65] = True
# dfs(0,0, 1)

from collections import deque
def bfs(r,c):
    global maximum
    alphabet_list = [0 for _ in range(26)]
    alphabet_list[ord(graph[r][c])-65] = 1
    q = deque([(r,c,alphabet_list)])
    while q:
        cur_r, cur_c, alphabet_list = q.popleft()
        for i in range(4):
            alpha = alphabet_list.copy()
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if next_r in range(R) and next_c in range(C) and alpha[ord(graph[next_r][next_c])-65]==0:
                alpha[ord(graph[next_r][next_c])-65] = 1
                q.append((next_r, next_c, alpha))
                maximum = max(maximum, sum(alpha))
bfs(0,0)


print(maximum)