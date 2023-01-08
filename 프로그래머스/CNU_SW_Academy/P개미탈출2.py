# 문제
# 길이가 N인 1차원 세상 , 왼쪽 or 오른쪽으로 이동 가능 , 최대 M개의 벽(#)을 부술 수 있다.
# .은 빈칸을 의미하고 빈칸은 자유롭게 이동 가능 , @(준식위치) 1번, O(탈출구)
# 준식이는 1차원 세상을 탈출 할 수 있을까요

# 입력
# 각 테스트 케이스의 첫째 줄에 1차원 세상의 길이 N (2 ≤ N ≤ 8) 와 준식이가 벽을 부술 수 있는 최대 횟수 M (0 ≤ M ≤ N - 2) 가 주어진다.
# 둘째 줄에 1차원 세상을 표현한 길이 N 짜리 문자열 S 가 주어진다.

# 출력
# 각 테스트 케이스마다 탈출가능 -> HAHA! // 탈출못함 -> HELP!

# 아이디어
# 

test = int(input())
for t in range(test):
    world_len, wall = map(int, input().strip().split())
    world = input()

    if world.index('@') <= world.index('O') + wall:
# count 함수 index() 에서 시작점 나오는 함수도 이용
# 왼쪽 오른쪽 가는 거니까 그 경우도 생각하기


