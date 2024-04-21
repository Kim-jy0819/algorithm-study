array = list(map(int, list(input())))

print(''.join(list(map(str, sorted(array, reverse=True)))))