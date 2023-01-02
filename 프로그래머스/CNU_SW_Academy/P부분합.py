# 문제
# int 형 배열이 입력되었을 때 부분 합을 계산하는 프로그램
# 배열 크기 N , 배열 요소인 정수 M이 N개 주어짐, 질의 Q, 네번째 줄부터 Q개의 정수 A,B가 줄마다 주어짐

# 입력예시
# 5 // 배열 크기 5개(N)
# 10 20 30 40 50 // 5개(N)의 정수(M)가 주어짐
# 5 // 질문 개수 5개(Q)
# 1 3 //첫번째 질문 : 배열에서 1(A) ~ 3(B)까지의 합 
# 2 4 //두번째 질문 : 배열에서 2(A) ~ 4(B)까지의 합 
# 3 5 //세번째 질문 : 배열에서 3(A) ~ 5(B)까지의 합 
# 1 5 //네번째 질문 : 배열에서 1(A) ~ 5(B)까지의 합 
# 4 4 //다섯번째 질문 : 배열 4번

# 아이디어
# list들의 각 부분합들에 대한 새로운 list를 만든다.
# 새로운 list의 첫번쨰 항이 0이 되어야 한다.
# M = [0 , num[0] , num[0]+num[1] , num[0]+num[1]+num[2], ...]

N = int(input())
num = list(map(int, input().split(' ')))
q = int(input())
S = [0]

for i in range(N):
    S.append(sum(num[0:i+1]))

for j in range(q):
    a, b = map(int, input().strip().split(' '))
    print(S[b]-S[a-1])