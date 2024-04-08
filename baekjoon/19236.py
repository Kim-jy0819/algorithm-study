import copy

graph = [[] for _ in range(4)]
direction = [[] for _ in range(4)]
coord = [(0,0) for _ in range(17)]
is_fish_live = [1 for _ in range(17)]

for i in range(4):
    input_data = list(map(int, input().split()))
    graph[i] = input_data[0::2]
    direction[i] = input_data[1::2]
for i in range(4):
    for j in range(4):
        node = graph[i][j]
        coord[node] = (i, j)
        direction[i][j] -= 1


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
def dfs(graph, coord, is_live, direction_lst):
    global maximum
    graph = copy.deepcopy(graph)
    coord = copy.deepcopy(coord)
    is_live = copy.deepcopy(is_live)
    direction_list = copy.deepcopy(direction_lst)
    for i in range(1, 17):
        if not is_live[i]:
            continue
        cur_x, cur_y = coord[i]
        direc = direction_list[cur_x][cur_y]
        nx, ny = cur_x + dx[direc], cur_y + dy[direc]
        for d_idx in range(8):
            if {nx, ny} < set(range(4)) and (nx, ny) != coord[0]:
                break
            direc = (direc + 1) % 8
            nx, ny = cur_x + dx[direc], cur_y + dy[direc]
        direction_list[cur_x][cur_y] = direc

        if d_idx == 7:
            continue

        # 물고기 자리 바꾸기
        graph[nx][ny], graph[cur_x][cur_y] = graph[cur_x][cur_y], graph[nx][ny]
        coord[i] = (nx, ny)
        if graph[cur_x][cur_y] in range(1,17):
            coord[graph[cur_x][cur_y]] = (cur_x, cur_y)

        direction_list[nx][ny], direction_list[cur_x][cur_y] = direction_list[cur_x][cur_y], direction_list[nx][ny]


    # import pprint
    # pprint.pprint(graph)
    # pprint.pprint(direction_list)

    s_cur_x, s_cur_y = coord[0]
    shark_direc = direction_list[s_cur_x][s_cur_y]
    for move_idx in range(1,4):
        shark_graph = copy.deepcopy(graph)
        shark_coord = copy.deepcopy(coord)
        is_live_after_shark = copy.deepcopy(is_live)
        snx, sny = s_cur_x + move_idx * dx[shark_direc], s_cur_y + move_idx * dy[shark_direc]
        if {snx, sny} < set(range(4)) and shark_graph[snx][sny] in range(1,17):
            is_live_after_shark[shark_graph[snx][sny]] = 0
            shark_graph[snx][sny] = 0
            shark_graph[s_cur_x][s_cur_y] = -1
            shark_coord[0] = (snx, sny)
            maximum = max(maximum, sum([fish_num for fish_num in range(1,17) if not is_live_after_shark[fish_num]]))
            # print(is_live_after_shark)
            dfs(shark_graph, shark_coord, is_live_after_shark, direction_list)

maximum = graph[0][0]
is_fish_live[graph[0][0]] = 0
graph[0][0] = 0

dfs(graph, coord, is_fish_live, direction)

print(maximum)