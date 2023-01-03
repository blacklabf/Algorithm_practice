# 문자열 앞뒤에 공백이 있어서 strip()을 사용해서 공백을 없앰 -> 왜!
# split(' ')이 아닌 split()을 쓰는 이유! 
# split()은 모든 공백을 한번에 처리하고 split(' ')는 공백 한 칸을 기준으로 나눈다.
# -> split(' ')하면 공백 2칸일 때 한 공백은 한 리스트에 담김
# strip() 안 써도 됨
sentence = input().strip().split()
print(len(sentence))

