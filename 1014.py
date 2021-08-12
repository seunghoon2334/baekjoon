def com(n):
    com1 = ['0']
    com2 = ['0','1']
    com3 = ['1','02']
    com4 = ['02','03','13']
    com5 = ['03','13','14','024']
    com6 = ['14','024','025','035','135']
    com7 = ['026','036','046','136','146','246']
    com8 = ['136','146','147','0246','0247','0257','0357','1357']
    com9 = ['147','0247','0257','0258','0357','0358','0368','1357','1358','1368','1468','02468']
    com10 = ['0258','0358','0368','0369','1358','1368','1369','1468','1469','1479','02468','02469','02479','02579','03579','13579']
    if n==1:
        return com1
    elif n==2:
        return com2
    elif n==3:
        return com3
    elif n==4:
        return com4
    elif n==5:
        return com5
    elif n==6:
        return com6
    elif n==7:
        return com7
    elif n==8:
        return com8
    elif n==9:
        return com9
    else:
        return com10

cnt = int(input())
for i in range(cnt):
    n,m = map(int, input().split(' '))
    max = 0
    combi = com(m)
    tables = []
    for j in range(n):
        table = input()
        tables.append(table)
    for k in combi:
        tmp = 0
        for l in k:
            for ii in range(n):
                if tables[ii][int(l)] == '.':
                    tmp += 1

        if tmp > max:
            max = tmp
    print(max)