a,b,c = map(int, input().split())

if a+b <= c or b+c <= a or c+a <= b:
    n = a+b+c - max(a,b,c)
    print(n + (n-1))
else:
    print(a+b+c)