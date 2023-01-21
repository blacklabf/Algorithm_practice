x = int(input())
n = int(input())
c = []
for i in range(n):
    a, b = map(int, input().split())
    c.append(a*b)
if sum(c) == x:
    print("Yes")
else:
    print("No")