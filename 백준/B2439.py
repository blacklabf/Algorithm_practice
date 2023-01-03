N = int(input())
for i in range(1, N+1):
    print(' ' * (N-i) + '*' * i )

# 공백 출력을 할 때 N-i 에다가 괄호를 안치니까 string으로 인식함