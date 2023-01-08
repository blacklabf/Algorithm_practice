# 문자열 S를 받아서 각 문자를 R번 반복해서 P를 출력함
# 입력
# 1) 테스트 케이스 T 2) 반복횟수 R 과 문자열 S

# C = A.append(B) 이렇게 해서 A(빈리스트)에다가 문자열을 추가해서 합치고 싶었는데
# append는 return(반환)하지 않고 바로 A 에다가 넣기 떄문에 위에 처럼 쓰는 게 아니라 A가 바뀌는 거다
# 함수마다 반환하는 값을 찾거나 반환하는지 알고 싶으면 마우스 올려봤을 때 none으로 나오면 반환 안 하는 함수

# 내 풀이
T = int(input())
for t in range(T):
    r , s = input().split()
    a = len(s)
    A = []
    for i in range(a):
        B = s[i] * int(r)
        A.append(B)
    print(''.join(A))
    
# 다른사람 풀이
T = int(input())
for t in range(T):
    R, S = input().split(' ') 
    P = ''
    for A in S: 
        P += int(R) * A 
    print(P)

