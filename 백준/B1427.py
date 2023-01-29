# 백준 소트인사이드
# 입력 : str로 받아서 slicing 하도록 하기 -> int로 받으면 slicing 안됨.
# 빈공간이 없는 입력값에 대해서는 오히려 split()을 해주면 split이 되지 않고 그 다음 list로 감싸도 한 문자로 저장되고 
# list에다가 바로 입력을 받아야 한문자씩 나눠서 저장
import sys; input = sys.stdin.readline
aList = list(input().strip())
aList.sort(reverse = True)
print(*aList, sep='')