# 백준 숫자 카드 2
# 이분탐색으로 풀기

# 이진 탐색 소스코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return count.get(target)
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)


import sys ; input = sys.stdin.readline
n = int(input().strip())
array = sorted(list(map(int, input().strip().split())))
m = int(input().strip())
target = list(map(int, input().strip().split()))

count = {}
for i in array:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in target:
    print(binary_search(array, i, 0, len(array)-1), end=' ')



