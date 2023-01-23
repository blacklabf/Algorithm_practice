# 백준 요세푸스 문제 0
import sys ; input = sys.stdin.readline
from collections import deque
queue = deque()
n, k = map(int, input().strip().split())
nList = list(range(1, n+1))
i = k-1
while len(nList) != 0:
    queue.append(nList[i])
    del nList[i]
    if len(nList) == 0 :
        break
    else: 
        i += k-1
        i = i % len(nList)

print("<", end='')
print(', '.join(map(str,list(queue))), end='')
print(">")







# import sys ; input = sys.stdin.readline
# n, m = map(int, input().strip().split())
# A = [i for i in range(1, n+1)]
# B = []

# while len(A) != 1:
#     if m == 1:
#         print(*A)
#     else:
#         for j in range(1, n):
#             if (m-1) * j < len(A)-1 :
#                 B.append(A[(m-1)*j])
#                 del A[(m-1)*j]
#             else:
#                 k = ((m-1)*j) % (len(A)-1)
#                 B.append(A[k-1])
#                 del A[k]
#         else:
#             B.append(A[0])

# print(B)



