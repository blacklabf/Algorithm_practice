N = int(input())
i = 2

while N != 1:
    if N % i != 0:
        i += 1
        continue
    else:
        print(i)
        N = N//i
        i = 2
