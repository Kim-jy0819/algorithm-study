N = int(input())

array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

array = sorted(array, key = lambda x : (x[0], x[1]))

for i in range(N):
    print(' '.join(list(map(str, array[i]))))