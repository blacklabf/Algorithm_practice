#split는 string에서만 자를 수 있으므로 str()로 바꿔줌
# if 가 아니라 for 써주는 거 주의하기! 
# N 안에 0부터 9까지 str로 정의되어있음
A = int(input())
B = int(input())
C = int(input())
N = list(str(A * B * C))

for i in range(10):
    print(N.count(str(i)))
