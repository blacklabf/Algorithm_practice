# 삼성 2056 : 연월일 달력
import sys; input = sys.stdin.readline
t = int(input())
dateDict = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
# dateDict = dict([(1,31),(2,28),(3,31),(4,30),(5,31),(6,30),(7,31),(8,31),(9,30),(10,31),(11,30),(12,31)])

for i in range(1, t+1):
    date = input().strip() # str로 입력받기 때문에 개행문자 제거
    year = date[:4]
    month = date[4:6]
    day = date[6:] 
    if 0 < int(month) < 13 and 0 < int(day) <= dateDict[int(month)]:
        print('#'+ str(i) +' '+ year + '/' + month + '/' + day)
        # print('#{} {}/{}/{}'.format(i, year,month,day))
    else : 
        print('#{} -1'.format(i))