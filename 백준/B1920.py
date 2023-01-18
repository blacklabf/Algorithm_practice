# 처음에 N_list를 유지한 상태로 M_list의 요소 개수를 세니까 시간초과 나옴
# M_list 통해서 나온 것들을 N_list에서 지워봄 -> 시간초과
# 다시 보니까 몇 개인지 세는게 아니라 있으면 1 없으면 0 출력임.
# 이분탐색 문제임 -> 다음에 도전!


# import sys ; input = sys.stdin.readline
# n = int(input())
# n_list = list(map(int, input().strip().split()))
# m = int(input())
# m_list = list(map(int, input().strip().split()))



# for i in range(len(m_list)):
#     if m_list



# for i in range(len(m_list)):
#     print(n_list.count(m_list[i]))
#     while m_list[i] in n_list:
#         n_list.remove(m_list[i])


# n = int(input())
# nList = list(map(int, input().strip().split()))
# m = int(input())
# mList = list(map(int, input().strip().split()))

# list = [0] * (100001)

# for num in nList:
#     list[num] = 1

# for number in mList:
#     if list[number] == 1:
#         print(1)
#     else:
#         print(0)

n = int(input())
nList = list(map(int, input().strip().split()))
m = int(input())
mList = list(map(int, input().strip().split()))

positiveList = [0] * (1000000000)
negativeList = [0] * (1000000000)

for num in nList:
    if num < 0:
        negativeList[abs(num)] = 1
    else:
        positiveList[num] = 1

for number in mList:
    if number < 0:
        if negativeList[abs(number)] == 1:
            print(1)
        else:
            print(0)
    else:
        if positiveList[abs(number)] == 1:
            print(1)
        else:
            print(0)

