import sys

tc = int(input())
for i in range(tc):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{i+1}: {a+b}')