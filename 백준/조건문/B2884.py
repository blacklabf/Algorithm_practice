# 처음에 M에 대한 조건만 생각해줬는데 0시 일 때의 조건도 생각해줘야 함 -> else 사용x
# M이 45이하일 때에만 H가 0일 때 음수가 나오므로 elif부터 H의 조건을 적어줌!
# H 가 0일 때는 == 쓰는 거 잊지 말기! ( = 아님! )
# 예제 입력 다 해보기! -> 코테때는 없으니까 잘 생각해보기!

# H, M = map(int, input().split(' '))
# if M >= 45:
#     print(H , M-45)
# else:
#     print(H-1 , M+15)


# 맞는 풀이
H, M = map(int, input().split(' '))
if M >= 45:
    print(H , M-45)
elif H > 0 and M < 45:
    print(H-1 , M+15)
elif H == 0 and M < 45:
    print(23 , M+15)