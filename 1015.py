cnt = int(input())
a = map(int, input().split(' '))
result = ''
for i in a:
    result += str(i-1) + ' '
print(result)