import sys
input = sys.stdin.readline

N = int(input())
stack = []
count = 0
for _ in range(N):
    input_temp = list(map(int, input().split()))
    if input_temp[0] == 1:
        stack.append(input_temp[1])
        count += 1
    elif input_temp[0] == 2:
        if count > 0:
            print(stack.pop())
            count -= 1
        elif count == 0:
            print(-1)
    elif input_temp[0] == 3:
        print(count)
    elif input_temp[0] == 4:
        if count > 0:
            print(0)
        elif count == 0:
            print(1)
    elif input_temp[0] == 5:
        if count > 0:
            print(stack[-1])
        elif count == 0:
            print(-1)
