# 내 풀이
a, b, c = map(int, input().split(' '))
N = [a, b, c]
n = N.count(a)
m = N.count(b)

if n == 3:
    print(10000 + a * 1000)
elif n == 2:
    print(1000 + a*100)
elif n == 1 and m == 2:
    print(1000 + b*100)
elif n == 1 and m == 1:
    print(max(a, b, c) * 100)

# 간단한 풀이
# if문에서 첫번째 조건이 아니면 elif로 넘어가는 거기 때문에
# a==b or b==c 조건에서 a==b==c일 수가 없음! -> 그리고 이 때에는 b가 같은 주사위
# a==c 에서도 첫번째 조건이 아니고 두번째 조건도 아니므로 a==b==c 일수가 없음
# 그 밖의 경우는 3개다 다를 수 밖에 없음
a,b,c=map(int,input().split())
if a==b==c:
    print(10000+a*1000)
elif a==b or b==c:
    print(1000+b*100)
elif a==c:
    print(1000+a*100)
else:
    print(max(a,b,c)*100)