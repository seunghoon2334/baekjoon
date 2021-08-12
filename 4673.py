def self_number(n):
    total = n
    for i in str(n):
        total += int(i)
    return total

numbers = [i for i in range(1,10001)]

for i in range(1,10001):
    selfi= self_number(i)
    if selfi < 10001:
        numbers[selfi-1] = 0

for j in numbers:
    if j != 0:
        print(j)