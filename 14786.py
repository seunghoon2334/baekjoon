import math
a, b, c = map(int,input().split())
min = -100000
max = 100000
min_val = a*min + b*math.sin(min)
max_val = a * max + b * math.sin(max)
if min_val==c:
    print(min)
elif max_val==c:
    print(max)
else:
    cnt = 0
    while True:
        x = (min + max)
        if x!=0:
            x /= 2
        x_val = a * x + b * math.sin(x)
        if x_val == c:
            print(x)
            break
        elif min_val < c < x_val:
            max = x
            max_val = x_val
        else:
            min = x
            min_val = x_val
        cnt += 1
        if abs(c - x_val) <= 0.000000001:
            print(x)
            break
