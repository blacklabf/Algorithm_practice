# 조건문에서 조건이 참이면 코드블럭을 실행하기 때문에 참이라는 boolean값이므로 and 사용 가능
score = int(input())
if score >=90 and score<=100:
    print('A')
elif score >=80 and score<90:
    print('B')
elif score >=70 and score<80:
    print('C')
elif score >=60 and score<70:
    print('D')
else:
    print('F')