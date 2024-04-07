a, b = map(int, input().split())

def num_generator(num):
    return [num]*num

interval = [0]
num = 1
while len(interval) < b+1:
    interval += num_generator(num)
    num += 1


result = 0
for i in range(a, b+1):
    result += interval[i]

print(result)
