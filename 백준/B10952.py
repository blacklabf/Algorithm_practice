# 백준 A+B-5 ; while -True 문과 break
while True:
    a, b = map(int, input().strip().split())
    if (a==0 and b==0):
        break
    else:    
        print(a+b)