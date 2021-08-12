import sys

tc = int(input())
for t in range(tc):
    H, W, N = map(int, sys.stdin.readline().split())

    YY = N % H
    if YY == 0:
        result = f'{H}'
    else:
        result = f'{YY}'

    XX = (N-1)//H
    if XX==9:
        result += '10'
    elif len(str(XX))==1:
        result += f'0{XX+1}'
    else:
        result += f'{XX+1}'

    print(result)



# 402 1203 101 303 302 9902 9901 9999 304 401

