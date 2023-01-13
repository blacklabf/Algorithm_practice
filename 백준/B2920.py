import sys ; input = sys.stdin.readline

music = list(map(int, input().strip().split()))

if music == [i for i in range(1, 9)]:
    print('ascending')
elif music == [j for j in range(8, 0, -1)]:
    print('descending')
else :
    print('mixed')

