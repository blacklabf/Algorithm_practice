# 백준 팩토리얼 0의 개수
import sys ; input = sys.stdin.readline
n = int(input())

def facto(a):
    if a > 1:
        return a * facto(a-1)
    else:
        return 1

cnt = 0
for i in range(len(str(facto(n)))-1, -1, -1):
    if str(facto(n))[i] == '0':
        cnt += 1
    else:
        print(cnt)
        break

