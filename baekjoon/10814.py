N = int(input())

array = []
for i in range(N):
    age, name = input().split()
    array.append((i, int(age), name))

array = sorted(array, key=lambda x:(x[1],x[0]))

for i in range(N):
    _, age, name = array[i]
    print(age, name)