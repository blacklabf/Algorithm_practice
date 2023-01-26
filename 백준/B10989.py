# 수 정렬하기3
# list의 천만개정도의 원소를 만개정도로 바꿔줌 -> 메모리초과 
import sys ; input = sys.stdin.readline
n = int(input())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(input())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)
