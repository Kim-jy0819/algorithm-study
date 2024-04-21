N = int(input())

array = [0 for _ in range(10001)]
for _ in range(N):
    num = int(input())
    array[num] = array[num] + 1


for i in range(1, 10001):
    for j in range(array[i]):
        print(i)
