a, b, c = map(int, input().split(' '))
N = [a, b, c]
n = N.count(a)
m = N.count(b)

if n == 3:
    print(10000 + a * 1000)
elif n == 2:
    print(1000 + a*100)
elif n == 1 and m == 2:
    print(1000 + b*100)
elif n == 1 and m == 1:
    print(max(a, b, c) * 100)