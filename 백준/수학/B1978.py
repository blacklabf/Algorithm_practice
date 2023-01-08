# # N 개 중에서 소수가 몇 개인지 찾기
# N = int(input())
# for i in range(N):
#     A = input().split()
# print(A)

a = []    # 빈 리스트 생성
 
for i in range(3):
    line = []              # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(2):
        line.append(0)     # 안쪽 리스트에 0 추가
    a.append(line)         # 전체 리스트에 안쪽 리스트를 추가
 
print(a)