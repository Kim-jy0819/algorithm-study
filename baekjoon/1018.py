N, M = map(int, input().split())

chess_board = [[['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']],
               [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]]


array = []
for _ in range(N):
    array.append(list(input()))

minimum = 1e9
for i in range(N-7):
    for j in range(M-7):
        for k in range(2):
            count = 0
            for l in range(8):
                for m in range(8):
                    if chess_board[k][l][m] != array[i+l][j+m]:
                        count += 1
            minimum = min(count, minimum)
print(minimum)
