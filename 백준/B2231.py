# list(map(int. str(n))) 이거랑 int(a) for a in str(n) 이랑 같음
N = int(input())
I = []
for i in range(N):
    n = list(map(int, str(i)))
    if i + sum(n) == N:
        I.append(i)

if I == []:
    print(0)
else:
    print(min(I))

