# 둘 다 split해서 list로 만들지 않았다
# 띄어쓰기로 구분되면 map함수를 쓰면 되는데 세자리 자연수를 한 숫자씩 split 해야해서 찾아보았다.
# 먼저 문자로 받은 다음 정수로 바꿔서 list로 만들어 주면 된다. comprehension

# 마지막에 합을 구할 때 자릿수를 생각해줘야 함 
# print(a*b[2]+a*b[1]+a*b[0]) 이렇게 하면 안됨

# 내가 푼 풀이
a = int(input())
num = input()
b = [int(i) for i in str(num)] # 357 입력하면 [3, 5, 7]이 되는데 정수로 됨
print(a*b[2])
print(a*b[1])
print(a*b[0])
print(a*b[2] + a*b[1]*10 + a*b[0]*100)

# 다른 사람 풀이
# 문자열로 받은 다음에 int로 각각 바꿔서 곱해줌

# A = int(input())  # 첫번째 입력받은 문자 : 숫자로 변환
# B = input()       # 두번째 입력받은 문자 : 문자열 그대로 둠

# # 문자열의 인덱스를 이용해서 두번째 입력 받은 문자를 하나씩 숫자로 반환하고 A와 곱한다.
# AxB2 = A * int(B[2])
# AxB1 = A * int(B[1])
# AxB0 = A * int(B[0])
# AxB = A * int(B)

# print(AxB2, AxB1, AxB0, AxB, sep='\n')
# # sep='\n'로 줄바꿈