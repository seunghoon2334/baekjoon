def sequence(num):
    chk = 10
    for i in range(len(str(num))-1):
        tmp = int(str(num)[i]) - int(str(num)[i+1])
        if chk == 10 :
            chk = tmp
        elif chk == tmp:
            continue
        else:
            return False
    return True

n = int(input())
result = 0
for i in range(1,n+1):
    if sequence(i):
        result += 1

print(result)