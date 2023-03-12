# 삼성 1936 : 1대1 가위바위보
import sys; input = sys.stdin.readline
a, b= map(int,input().strip().split())
dic = {1:3, 2:1, 3:2}
if dic[a] == b:
    print('A')
else:
    print('B')