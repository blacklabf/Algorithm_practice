# 사칙연산
import sys ; input = sys.stdin.readline
t = int(input())
for i in range(t):
    a = list(input().strip().split())
    if '*' in a:
        if int(a[4]) == int(a[0]) * int(a[2]):
            print('correct')
        else :
            print('wrong answer')
    if '+' in a:
        if int(a[4]) == int(a[0]) + int(a[2]):
            print('correct')
        else :
            print('wrong answer')
    if '-' in a:
        if int(a[4]) == int(a[0]) - int(a[2]):
            print('correct')
        else :
            print('wrong answer')
    if '/' in a:
        if int(a[4]) == int(a[0]) / int(a[2]):
            print('correct')
        else :
            print('wrong answer')
