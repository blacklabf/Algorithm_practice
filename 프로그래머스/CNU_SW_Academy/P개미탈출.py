# 벽이 1개 이하여야 한다.
S = input()
if S.count('#') > 1:
    print('HELP!')
else:
    print('HAHA!')