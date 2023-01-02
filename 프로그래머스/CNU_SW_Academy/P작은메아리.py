# 문제
# 두 개의 빵의 가격과 이름이 주어질 때 더 비싼 빵의 이름 출력

# 입력
# 첫째 줄 : 첫번째 빵 이름 (길이 10 이하의 알파벳 대소문자)
# 둘째 줄 : 첫번째 빵 가격 A (정수)
# 셋째 줄 : 두번째 빵 이름
# 넷째 줄 : 두번째 빵 가격 B

a = input()
A = int(input())
b = input()
B = int(input())

if A > B:
    print(a)
else:
    print(b)