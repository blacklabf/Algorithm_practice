# 문자열 여러줄 입력받기
# 처음에 input()으로 받은 걸 int로 바꿔줬어야 함.
# 첫번째 줄 만으로도 list로 나옴

# 틀린 풀이 
A = [int(input()) for _ in range(9)]
A_list = list(A)
B = max(A_list)
print(B)
print(A_list.index(B) + 1 )

# 맞는 풀이
A = [int(input()) for _ in range(9)]
B = max(A)
print(B)
print(A.index(B) + 1 )