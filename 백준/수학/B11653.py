# N = int(input())
# a = []
# if N == 1:
#     pass
# else:
#     for i in range(2,N+1):
#         if N % i != 0:
#             continue
#         else:
#             print(i)
#             N = N // i

N = int(input())
i = 2

while N != 1:
    if N % i != 0:
        i += 1
        continue
    else:
        print(i)
        N = N//i
        i = 2



