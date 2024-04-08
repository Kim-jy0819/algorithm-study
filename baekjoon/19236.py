graph = [[] for _ in range(4)]
direction = [[] for _ in range(4)]
coord = [(0,0) for _ in range(17)]
for i in range(4):
    input_data = list(map(int, input().split()))
    graph[i] = input_data[0::2]
    direction[i] = input_data[1::2]
for i in range(4):
    for j in range(4):
        node = graph[i][j]
        coord[node] = (i, j)

maximum = graph[0][0]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
def dfs(x, y):
    global maximum

    for i in range(1, 17):
        cur_x, cur_y = coord[i]
        direc = direction[cur_x][cur_y]
        nx, ny = x+dx[direc], y+dy[direc]
        for _ in range(8):
            if nx in range(16) and ny in range(16) and (nx, ny) != coord[0]:

                break
            direc = (direc+1)%8


