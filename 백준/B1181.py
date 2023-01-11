import sys ; input = sys.stdin.readline
N = int(input())
a = [input().strip() for _ in range(N)]
a = list(set(a))
a.sort()
a.sort(key=lambda x: len(x))
print(*a, sep='\n')

# 출력할 때 아래처럼 해도 됨
# for i in a
    #print(a)