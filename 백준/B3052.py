# 나머지
num = [int(input()) for _ in range(10)]
rest = []
for i in range(10):
    rest.append(num[i] % 42)

print(len(set(rest)))