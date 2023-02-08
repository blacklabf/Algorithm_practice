# 백준 숫자카드
# 이진탐색
# 여기서는 무조건 split 해야 함, str로 받으면 안됨
import sys; input = sys.stdin.readline
n = int(input()) # 숫자 카드의 개수 : N
nList = list(map(int, input().strip().split())) # 상근이가 가지고 있는 숫자카드
m = int(input()) # 정수 M개
mList = list(map(int, input().strip().split())) # 상근이가 가지고 있는지 확인

ans = []

# 이진 탐색 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for num in mList:
    result = binary_search(nList, num, 0, n - 1)
    if result == None:
        ans.append(0)
    else:
        ans.append(1)

print(*ans, sep=' ')



