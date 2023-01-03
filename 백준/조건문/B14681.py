# 마지막에 else 안하고 elif한 이유는 0인 경우를 제외하기 위해서
# 예제 입력을 확인하고 한 줄로 입력했는지 각각 입력했는지 확인해서 입력 코드를 적어야 한다.
# x, y = map(int, input().split('')) -> 이거는 한 줄로 입력하는 경우

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)