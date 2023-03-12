# 삼성 2056 : 연월일 달력
import sys; input = sys.stdin.readline
t = int(input())
for i in range(1, t+1):
    date = input().strip()
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]
    if int(month) == 0 :
        print('#{} -1'.format(i))
    elif int(month) == 2:
        if int(day) >= 29 :
            print('#{} -1'.format(i))
        else :
            print('#{} {}/{}/{}'.format(i, year,month,day))
    elif int(month) % 2 == 0:
        if int(day) > 30 :
            print('#{} -1'.format(i))
        else : 
            print('#{} {}/{}/{}'.format(i, year,month,day))
    elif int(month) % 2 != 0 :
        if int(day) > 31:
            print('#{} -1'.format(i))
        else :
            print('#{} {}/{}/{}'.format(i, year,month,day))