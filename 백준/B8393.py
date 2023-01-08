# # 1부터 n까지의 합
n = int(input())
S = []
for i in range(1, n+1):
    S.append(i)
print(sum(S))

# 자연수의 합 공식
n = int(input())
print(int((n * (n+1))/2))