import sys

a, b, c = map(int, sys.stdin.readline().split())

if b < c:
    result = a//(c-b) + 1
else:
    result = -1

print(result)