# 삼성 2058 : 자릿수 더하기
import sys ; input = sys.stdin.readline
nList = input().strip()
nSum = sum(list((map(int, nList))))
print(nSum)