import sys ; input = sys.stdin.readline
score = [int(input()) for _ in range(5)]
for i in range(5):
    if score[i] < 40:
        score[i] = 40
    else:
        pass

print(int(sum(score)/5))