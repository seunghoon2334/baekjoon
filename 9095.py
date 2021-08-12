def one(req, n):
    global result
    req += 1
    if req == n:
        result += 1
        return False
    elif req > n:
        return False
    else:
        return req

def two(req, n):
    global result
    req += 2
    if req == n:
        result += 1
        return False
    elif req > n:
        return False
    else:
        return req

def three(req, n):
    global result
    req += 3
    if req == n:
        result += 1
        return False
    elif req > n:
        return False
    else:
        return req

def ott(req, n):
    global result
    one_val = one(req, n)
    two_val = two(req, n)
    three_val = three(req, n)
    if one_val:
        ott(one_val, n)
    if two_val:
        ott(two_val, n)
    if three_val:
        ott(three_val, n)
    return

T = int(input())
for t in range(T):
    n = int(input())
    global result
    result = 0
    ott(0, n)
    print(result)