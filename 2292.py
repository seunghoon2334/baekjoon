num = int(input())

tmp = 1
distance = 1
while True:
    if num > tmp:
        tmp += 6*distance
        distance += 1
    else:
        print(distance)
        break