# 백준 체스판 다시 칠하기
# 주어진 입력값에서 자르는게 아니라 새로운 list에다가 넣는다는 생각!
# if -if 랑 if - elif 차이
import sys ; input = sys.stdin.readline
a, b = map(int, input().strip().split())
aList = [input().strip() for _ in range(a)]
chess = []

for i in range(a-7):
    for j in range(b-7):
        fw = 0
        fb = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if aList[k][l] != 'W':
                        fw += 1
                    if aList[k][l] != 'B':
                        fb += 1
                else:
                    if aList[k][l] != 'B':
                        fw += 1
                    if aList[k][l] != 'W':
                        fb += 1
        chess.append(fw)
        chess.append(fb)
print(min(chess))


