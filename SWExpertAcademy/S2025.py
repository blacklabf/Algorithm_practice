# 삼성 2025 : N줄덧셈
import sys; input = sys.stdin.readline
num = int(input())
ans = 0
for i in range(1, num+1):
    ans += i
    print(ans)