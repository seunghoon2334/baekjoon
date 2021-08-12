import sys

cnt, num = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
result = ''
for idx,i in enumerate(numbers):
    if i < num:
        result += str(i) + ' '
print(result.rstrip())