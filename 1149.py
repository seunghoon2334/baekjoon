global N, RGB, result, min_cost
result = 1000001
N = int(input())
RGB = dict()

def rcolor(cnt, tmp):
    global N, result, min_cost
    tmp += RGB[cnt]['R']
    if tmp >= result:
        return
    elif cnt==N-1:
        result = tmp
        return
    elif not (tmp + min_cost > result):
        gcolor(cnt+1, tmp)
        bcolor(cnt+1, tmp)
    return

def gcolor(cnt, tmp):
    global N, result, min_cost
    tmp += RGB[cnt]['G']
    if tmp >= result:
        return
    elif cnt==N-1:
        result = tmp
        return
    elif not (tmp + min_cost > result):
        rcolor(cnt+1, tmp)
        bcolor(cnt+1, tmp)
    return

def bcolor(cnt, tmp):
    global N, result, min_cost
    tmp += RGB[cnt]['B']
    if tmp >= result:
        return
    elif cnt==N-1:
        result = tmp
        return
    elif not (tmp+min_cost > result):
        rcolor(cnt+1, tmp)
        gcolor(cnt+1, tmp)
    return

def color(cnt, tmp):
    rcolor(cnt, tmp)
    gcolor(cnt, tmp)
    bcolor(cnt, tmp)

min_cost = 1000
for i in range(N):
    R,G,B = map(int,input().split(' '))
    RGB.update({i:{'R':R,'G':G,'B':B}})
    min_cost = min(min_cost,R,G,B)

color(0, 0)
print(result)