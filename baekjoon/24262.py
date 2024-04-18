from itertools import combinations

N, M = map(int, input().split())

array = list(map(int, input().split()))
all_cases = combinations(array, 3)

maximum = 0
for combi in all_cases:
    result = sum(combi)
    if result <= M:
        maximum = max(maximum, result)
print(maximum)