# map : list들의 값을 split으로 쪼개서 각각의 값으로 나오게 함.
# 다시 list()를 해서 그 값들의 새로운 list를 만들어 줌.
# 다시 list로 하는 이유는 input().split(' ')하면 list로 나오지만 string의 값이기 때문에
# map을 통해 int로 바꿔주고 list를 다시 해서 int들의 list로 만들어줌
N = int(input())
score = list(map(int, input().split(' ')))
A = max(score)

new_average = (sum(score) * 100 / A) / N
print (new_average)