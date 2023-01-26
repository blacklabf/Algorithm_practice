# 나무조각
# for문을 제대로 사용 -> 그냥 막 쓰면 안됨.
# print가 if랑 있으면 안바뀌어도 출력 , for문이랑 있으면 다 바뀐다음에 출력
import sys ; input = sys.stdin.readline
tree = list(map(int, input().strip().split()))
while tree != [1, 2, 3, 4, 5]:
    for i in range(4):
        if tree[i] > tree[i+1]:
            tree[i], tree[i+1] = tree[i+1], tree[i]
            print(*tree)