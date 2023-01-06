N = int(input())
p = 1
start = 1
while N > start :
    start += 6*p
    p += 1
print(p)
