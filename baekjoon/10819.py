# max min max min max min max
# 10 1 20 4 15 8
# 9 19 16 11 7   28 44 55

from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))

occasions = permutations(arr, N)

def calc(arr):
    result = 0
    for i in range(len(arr)-1):
        result+=abs(arr[i+1] - arr[i])

    return result
maximum = 0
for occ in occasions:
    result = calc(occ)
    maximum = max(maximum, result)
print(maximum)
