N = int(input())

def find_generator(N):
    min_ = max(N-54, 1)
    for generator in range(min_,N+1):
        each_num_sum = sum(map(int, list(str(generator))))
        if N == each_num_sum + generator:
            return generator
    return 0

print(find_generator(N))
