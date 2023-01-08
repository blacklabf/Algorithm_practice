# # 런타임 에러
# n = list(input())
# while n != ['0']:
#     for i in range(len(n)):
#         if n[i] == n[len(n)-1-i]:
#             print('yes')
#         else :
#             print('no')
#         n = list(input())

# 배열 뒤집기
n = input()
while n != '0':
    if n[::] == n[:: -1]:
        print("yes")
    else:
        print("no")
    n = input()