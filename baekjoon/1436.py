N = int(input())

title = [0 for _ in range(10001)]
n = 1
i = 1
while n <= N:
    if '666' in str(i):
        title[n] = i
        n += 1
    i += 1
print(title[N])