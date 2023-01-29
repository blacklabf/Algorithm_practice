# 백준 OX 퀴즈
# list 배열로 받기, print의 실행위치, 아이디어 생각, for문에 인덱스번호 대신 문자열로 가능
# 변수 선언할 때 int형넣기, 리터럴문자, 숫자(2,8,10 진법)
import sys ; input = sys.stdin.readline
test = int(input())
for i in range(test):
    lis = list(map(str, input().strip()))
    count = 1
    sum = 0
    for j in lis:
        if j == 'O':
            sum += count
            count += 1
        else:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
            count = 1
    print(sum)


