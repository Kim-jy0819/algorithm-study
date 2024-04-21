N = int(input())

array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

array = sorted(array, key = lambda x : (x[1], x[0]))

for i in range(N):
    print(' '.join(list(map(str, array[i]))))