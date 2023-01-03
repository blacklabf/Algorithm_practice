# 둘 다 split해서 list로 만들지 않았다
# 띄어쓰기로 구분되면 map함수를 쓰면 되는데 세자리 자연수를 한 숫자씩 split 해야해서 찾아보았다.
# 먼저 문자로 받은 다음 정수로 바꿔서 list로 만들어 주면 된다. comprehension

# 마지막에 합을 구할 때 자릿수를 생각해줘야 함 
# print(a*b[2]+a*b[1]+a*b[0]) 이렇게 하면 안됨

a = int(input())
num = input()
b = [int(i) for i in str(num)] # 357 입력하면 [3, 5, 7]이 되는데 정수로 됨
print(a*b[2])
print(a*b[1])
print(a*b[0])
print(a*b[2] + a*b[1]*10 + a*b[0]*100)