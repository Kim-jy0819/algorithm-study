N = int(input())

word_set = set([])
for _ in range(N):
    word_set.add(input())
array = list(word_set)
array = sorted(array, key = lambda x : (len(x), x))

for i in range(len(array)):
    print(array[i])