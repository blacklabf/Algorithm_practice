# 문자열 S를 받아서 각 문자를 R번 반복해서 P를 출력함
# 입력
# 1) 테스트 케이스 T 2) 반복횟수 R 과 문자열 S

T = int(input())
for t in range(T):
    R, S = input().split(' ') # R, S 모두 string 형으로 출력
    P = ''
    for A in S: #이때 S가 abc 이면 A는 순차적으로 a, b, c
        P += int(R) * A # P를 위에서 먼저 정의해줘야 함.
    print(P)
        




