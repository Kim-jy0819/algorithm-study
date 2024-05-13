N = int(input())
sangkeun = dict(zip(list(map(int, input().split())))
M = int(input())
num_set = dict(zip(list(map(int, input().split())),[-1] * M))
result = ''
for i in num_set:

    if {i} <= sangkeun:
        result += ' 1'
    else:
        result += ' 0'

print(result.strip())