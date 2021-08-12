import sys

A, B, V = map(int, sys.stdin.readline().split())
C = A - B # 하루에 오르는 높이
height = V-A

days = 1
if height > 0:
    if height%C == 0 :
        days += height//C
    else:
        days += (height//C) + 1

print(days)