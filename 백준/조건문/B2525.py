# (A+D) >=24 이면 무조건 B+C >= 60 일 수밖에 없음

A, B = map(int, input().split(' '))
C = int(input())
D = (B + C) // 60

if (A+D) >= 24:
    print(A+D-24, B+C-(60*D))
elif (A+D) < 24 and (B+C) >= 60:
    print(A+D , B+C-(60*D))
elif (A+D) < 24 and (B+C) < 60:
    print(A+D , B+C)