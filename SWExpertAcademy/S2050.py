# 삼성 2050 : 알파벳을 숫자로 변환
import sys ; input = sys.stdin.readline
aList = input().strip()
for a in aList:
    print(ord(a)-64 , end=' ')