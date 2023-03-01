# 백준 1541 : 잃어버린괄호(그리디,파싱)
import sys ; input = sys.stdin.readline
aList = input().strip().split('-')
num = 0
for i in aList[0].split('+'):
    num += int(i)
for j in aList[1:]:
    for k in j.split('+'):
        num -= int(k)
print(num)