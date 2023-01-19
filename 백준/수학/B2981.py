# 메모리초과
# N = int(input())
# rem = []
# b = []
# num_list = [input() for _ in range(N)]
# for i in range(len(num_list)):
#     a = []
#     for j in range(2, int(min(num_list))+1):
#         a.append(int(num_list[i]) % j)
#     rem.append(a)
# for y in range(int(min(num_list))-1):
#     new_rem = []
#     for x in range(N):
#         new_rem.append(rem[x][y])
#     b.append(new_rem)

# answer = []
# for m in range(int(min(num_list))-i):
#     if min(b[m]) * N == sum(b[m]):
#         answer.append(m+2)

# print(*sorted(answer))

# # 풀이 2 -> 시간을 최대한 줄여보기

# import sys ; input = sys.stdin.readline
# import math

# n = int(input())
# n_list = [int(input()) for _ in range(n)]
# #n_list.sort()
# m_list = []
# gcd_list = []

# for i in range(n-1):
#     m_list.append(n_list[i+1] - n_list[i])

# m_list = list(set(m_list)) # 중복제거
# n = math.gcd(*m_list)
# for i in range(2, math.sqrt(n)+1):
#     if n %i == 0: print(i, end=' ')






# # 풀이 2 -> 시간을 최대한 줄여보기

# import sys ; input = sys.stdin.readline
# import math

# n = int(input())
# n_list = [int(input()) for _ in range(n)]
# n_list.sort()
# m_list = []
# gcd_list = []

# for i in range(n-1):
#     m_list.append(n_list[i+1] - n_list[i])

# m_list = list(set(m_list)) # 중복제거
# n = math.gcd(*m_list)
# if n == 1:
#     print(1)
# else:
#     for i in range(2, int(math.sqrt(n))+1, 1):
#         if n %i == 0: 
#             gcd_list.append(i)
#             gcd_list.append(n // j)
#     print(gcd_list)

# 풀이 3 
# N = int(input())
# num = sorted([int(input()) for _ in range(N)])
# re_num = []

# for i in range(1, N):
#     re_num.append(num[i] - num[i-1])

# def findGCD(a, b):
#     num = b
#     div = a
#     rest = num % div
#     while rest != 0:
#         num = div
#         div = rest
#         rest = num % div
#     return div

# GCD = re_num[0]
# for idx in range(1, len(re_num)):
#     GCD = findGCD(GCD, re_num[idx])

# result = set()
# for i in range(2, int(GCD**0.5) + 1):
#     if GCD % i == 0:
#         result.add(i)
#         result.add(GCD // i)
# result.add(GCD)
# print(*sorted(list(result)))


import sys ; input = sys.stdin.readline
import math

n = int(input())
n_list = [int(input()) for _ in range(n)]
n_list.sort()
m_list = []
gcd_list = []

for i in range(n-1):
    m_list.append(n_list[i+1] - n_list[i])

m_list = list(set(m_list)) # 중복제거
n = math.gcd(*m_list)
for i in range(1, int(math.sqrt(n))+1, 1):
    if n %i == 0: 
        gcd_list.append(i)

Gcd_list = []

for j in gcd_list:
    Gcd_list.append(n // j)

answer = list(set(Gcd_list + gcd_list))
answer.sort()

answer.remove(1)



print(*sorted(answer))



# answer = sorted(list) 를 하면 오름차순으로 정렬된 list를 answer로 받는 거고
# list.sort() 하면 list 자체를 sort 하는 거
# -> answer = list.sort() 하면 나오지 않음