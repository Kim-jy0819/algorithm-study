import itertools

N, M = map(int, input().split())

arr = list(range(1,N+1))
occasions = itertools.permutations(arr, M)
occasions = sorted(occasions)
for occ in occasions:
    print(*occ)
