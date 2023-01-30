# 백준 분수찾기 1193

# 아이디어 1
# 1, 2, 3, 4, 5 이렇게 개수로 dict로 함 
# x는 피보나치로 구현할수 있음 1+2+3+4 이렇게 한 다음 가장 바로 직전인 거에 다음 줄로 가서 나머지 만큼 움직여줌
# key가 중복되면 안되니까 안 된다고 생각

# 아이디어 2 
# 리스트를 분자, 분모 2개로 만들어서 append를 해줌
# 각각 리스트는 인덱스를 1부터 생각해주려고 0을 먼저 넣어줌
# 출력할 때 각각 가져옴
# 시간초과가 나올 거 같음

# 아이디어 3
# 가운데 줄을 기준으로 생각 -> 짝수일 떄 가운데가 없음

# 아이디어 4
# 피보나치 사용 

import sys; input = sys.stdin.readline
x = int(input())
n = 0 #분자
m = 0 #분모
a = 0

def fibo(z):
    if z == 1 or z == 2:
        return 1
    elif z == 0:
        return 0
    return fibo(z - 1) + fibo(z - 2)

for i in range(1, x+1):
    if fibo(i) >= x:
       a += i
       break
    else:
        pass 

c = x - fibo(a-1)

if a % 2 != 0 :
    n += a - (c-1)
    m += c
else:
    n += c
    m += a - (c-1)

print(n , '/' , m)


