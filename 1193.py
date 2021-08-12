X = int(input())

tmp = 1
cnt = 2
while True:
    if X > tmp:
        tmp += cnt
        cnt += 1
    elif cnt%2 == 0:
        print(f'{tmp-X+1}/{cnt-tmp+X-1}')
        break
    else:
        print(f'{cnt-tmp+X-1}/{tmp-X+1}')
        break