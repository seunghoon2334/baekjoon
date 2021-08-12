# import math
# a, b, c = map(int,input().split())
# min = -100000
# max = 100000
# min_val = a*min + b*math.sin(min)
# max_val = a * max + b * math.sin(max)
# if min_val==c:
#     print(min)
# elif max_val==c:
#     print(max)
# else:
#     cnt = 0
#     while True:
#         x = (min + max)
#         if x!=0:
#             x /= 2
#         x_val = a * x + b * math.sin(x)
#         if min_val==x_val or x_val==max_val:
#             print(round(x,6))
#             break
#         if x_val == c:
#             print(round(x,6))
#             break
#         elif min_val < c < x_val:
#             max = x
#             max_val = x_val
#         else:
#             min = x
#             min_val = x_val
#         cnt += 1
#         if abs(c - x_val) <= 1e-20:
#             print(round(x,6))
#             break
from scipy.optimize import fsolve
import math
a,b,c = map(int,input().split())
f = lambda x: a*x + b*math.sin(x) -c
sol = fsolve(f, -100000)
print(round(sol[0],6))