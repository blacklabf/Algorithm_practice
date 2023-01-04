N = int(input())
score = list(map(int, input().split(' ')))
A = max(score)

new_average = (sum(score) * 100 / A) / N
print (new_average)