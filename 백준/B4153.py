tri = list(map(int, input().split()))
tri.sort()
while tri != [0, 0, 0]:
    if (tri[0] ** 2) + (tri[1] ** 2) == (tri[2] ** 2):
        print("right")
    else:
        print("wrong")
    tri = list(map(int, input().split()))
    tri.sort()

# 이렇게 해도 되고 while True: 방법도 있음 